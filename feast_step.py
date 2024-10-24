#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.Prepare Data Set
#2.feast init
#3.Update feature store
#4.Define feature definition
#5.feast apply
#6.Generate Trainning data set
#7.Model Training
#8.Prepare online feature store
import pandas as pd
from feast.types import Int64


# In[2]:


from pathlib import Path

# Definir a raiz do projeto
BASE_DIR = Path("ifood").resolve().parent
print(f'Diretorio encontrado: {BASE_DIR}')

# In[3]:


df = pd.read_csv('feature_repo/data/restaurant.csv')


# In[4]:


df.head()


# In[5]:


# Convertendo a coluna de string para datetime
df['datetime_col'] = pd.to_datetime(df['created_at'], format='%Y-%m-%dT%H:%M:%S.%fZ')

# Convertendo a coluna de string para timestamp
# Dividindo por 10^9 para obter o timestamp em segundos
df['timestamp_col'] = df['datetime_col'].astype('int64') // 10**9  


# In[6]:


#Change dataset to Parquet
df.to_parquet(path='feature_repo/data/restaurant.parquet')


# In[7]:


df.head()


# In[8]:


#!feast apply


# In[9]:


#Trainning dataset
from feast import FeatureStore
from feast.infra.offline_stores.file_source import SavedDatasetFileStorage

store = FeatureStore(repo_path=f'{BASE_DIR}/feature_repo')

entity_df = pd.read_parquet(path = 'feature_repo/data/restaurant.parquet')

training_data = store.get_historical_features(
entity_df = entity_df,
    features = [
        "restaurant_fview:enabled",
        "restaurant_fview:price_range",
        "restaurant_fview:average_ticket",
        "restaurant_fview:takeout_time",
        "restaurant_fview:delivery_time",
        "restaurant_fview:minimum_order_value",
        "restaurant_fview:merchant_zip_code",
        "restaurant_fview:merchant_city",
        "restaurant_fview:merchant_state",
        "restaurant_fview:merchant_country"
    ]
)

dataset = store.create_saved_dataset(
from_=training_data,
    name = "restaurant_dataset",
    storage = SavedDatasetFileStorage('feature_repo/data/restaurant_dataset1.parquet')
)


# In[10]:


#Training Show
training_data.to_df()


# In[11]:


#Model training
# Importing dependencies
from feast import FeatureStore
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from joblib import dump

# Getting our FeatureStore
store = FeatureStore(repo_path=f'{BASE_DIR}/feature_repo')

# Retrieving the saved dataset and converting it to a DataFrame
training_df = training_data.to_df() #store.get_saved_dataset(name="restaurant_dataset").to_df()
#training_df = training_df.dropna(subset=['price_range'])

# Separating the features and labels
y = training_df['price_range']
X = training_df.drop(
    labels=['price_range', 'datetime_col', "id"], 
    axis=1)

# Apply One-Hot Encoding to all categorical columns
# ValueError: could not convert string to float: '2017-01-20T13:14:42.202Z'
X = pd.get_dummies(X, drop_first=True)

# Splitting the dataset into train and test sets
#X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

# Remover valores ausentes
X_train = X_train.dropna()
y_train = y_train[X_train.index] 

# Creating and training LogisticRegression
reg = LogisticRegression(max_iter = 200)
reg.fit(X=X_train, y=y_train)

# Saving the model
dump(value=reg, filename="model/model.joblib")


# In[12]:


# Ver tipo de cada coluna
#print(X.dtypes)

# Contar vazios
print(X_train.isnull().sum())


# In[16]:


#Materialized
#Prepare Online Feature Store
# Importing dependencies
from feast import FeatureStore
from datetime import datetime, timedelta

# Getting our FeatureStore
store = FeatureStore(repo_path=f'{BASE_DIR}/feature_repo')

store.materialize_incremental(end_date = datetime.now())

#store.materialize(start_date=datetime.utcnow() - timedelta(days=530), end_date=datetime.utcnow() - timedelta(days=10))


# In[18]:


#Get online features
# Importing dependencies
from feast import FeatureStore
import pandas as pd
from joblib import load

# Getting our FeatureStore
store = FeatureStore(repo_path=f'{BASE_DIR}/feature_repo')

# Defining our features names
feast_features = [
        "restaurant_fview:enabled",
        "restaurant_fview:price_range",
        "restaurant_fview:average_ticket",
        "restaurant_fview:takeout_time",
        "restaurant_fview:delivery_time",
        "restaurant_fview:minimum_order_value",
        "restaurant_fview:merchant_zip_code",
        "restaurant_fview:merchant_city",
        "restaurant_fview:merchant_state",
        "restaurant_fview:merchant_country",
    ]

# Getting the latest features
features = store.get_online_features(
    features=feast_features,    
    entity_rows=[{"id": '2458597b6740ab52e6834cb92b07072feba38ef303f4676575ab963513275b3b'}, {"id": 'ac47c7dde8af939606999bd912979082f0c2667a0bc0183712375b5f9ca40fc7'}]
).to_dict()

# Converting the features to a DataFrame
features_df = pd.DataFrame.from_dict(data=features)


# In[19]:


features_df.head()


# In[20]:


# Loading our model and doing inference
#reg = load("model.joblib")
#predictions = reg.predict(features_df[sorted(features_df.drop("id", axis=1))])
#print(predictions)

def load_model(model_path):
    """Carrega o modelo treinado."""
    try:
        model = load(model_path)
        print(f"Modelo carregado com sucesso de {model_path}")
        return model
    except Exception as e:
        print(f"Erro ao carregar o modelo: {e}")
        raise
    
def preprocess_features(features_df):
    """Pré-processa o DataFrame de features para garantir que as colunas estejam corretas."""
    try:
        # Remover a coluna 'id' e ordenar as colunas para garantir compatibilidade com o modelo
        preprocessed_features = features_df.drop("id", axis=1)
        preprocessed_features = preprocessed_features[sorted(preprocessed_features.columns)]
        
        # Verificar se há valores nulos
        if preprocessed_features.isnull().sum().sum() > 0:
            raise ValueError("Há valores nulos nas features fornecidas.")
        
        return preprocessed_features
    except Exception as e:
        print(f"Erro durante o pré-processamento das features: {e}")
        raise
    
def make_predictions(model, features_df):
    """Realiza previsões usando o modelo treinado e as features fornecidas."""
    try:
        predictions = model.predict(features_df)
        return predictions
    except Exception as e:
        print(f"Erro ao fazer previsões: {e}")
        raise

# Caminho do modelo treinado
model_path = "model/model.joblib"

# Carregar o modelo treinado
reg = load_model(model_path)

# Pré-processar as features
features_df_preprocessed = preprocess_features(features_df)

# Realizar as previsões
predictions = make_predictions(reg, features_df_preprocessed)

# Exibir as previsões
print(predictions)


# In[21]:


#API FasAPI
#Definir Caminho para Chamar API
# Definir a raiz do projeto da API
BASE_DIR_API = f'{BASE_DIR}' 

print(f'Diretorio api: {BASE_DIR_API}')


# In[23]:


#Iniciar a API via linha de comando (cmd/terminal)
#acessar o diretorio api onde está o arquivo main.py
#executar o comando abaixo. Trocar a porta para 9000 em caso de conflito
get_ipython().system('uvicorn main:app --reload --port 8080')


# In[ ]:


#Após executar API, acessar a documentação em: http://localhost:8080/docs

