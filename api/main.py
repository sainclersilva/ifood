from fastapi import FastAPI
from parso.python.tree import String
from pydantic import BaseModel
import joblib
import numpy as np
import os

# Definir a raiz do projeto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath('__init__.py')))
print(f'Diretorio encontrado: {BASE_DIR}')
# Load the trained model
model = joblib.load(f'{BASE_DIR}/model/model.joblib')
print(f'Modelo encontrado: {model}')

app = FastAPI()

class PredictRequest(BaseModel):
    price_range: int
    average_ticket: float
    takeout_time: int
    delivery_time: float
    minimum_order_value: float
    merchant_zip_code: int

# Define the prediction endpoint
@app.post("/predict")
def predict(request: PredictRequest):
    data = np.array([[request.price_range,
                      request.average_ticket,
                      request.takeout_time,
                      request.delivery_time,
                      request.minimum_order_value,
                      request.merchant_zip_code]])
    prediction = model.predict(data)
    species_map = {0: 'Male', 1: 'Female'}
    #species_map = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
    return {"prediction": species_map[int(prediction[0])]}

# This will start the server API at http://127.0.0.1:8000.

#command uvicorn main:app --reload0

@app.get("/")
def read_root():
    return {"message": "Welcome to the Restaurant API"}

# Documentation at http://127.0.0.1:8000/docs