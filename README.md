### 1. Informções do projeto
Feature Store Project with FastAPI

### 2. Requisitos do Sistema
- **Python 3.12.7**: Certifique-se de ter o Python 3.12.7 instalado. 
- **pip**: Instalador de pacotes do Python (geralmente já vem com a instalação do Python).
- **Virtualenv**: (Opcional, mas recomendado) para isolar dependências.
- **PyCharm 2024.2.3** (IDE recomendada) ou VSCode


### 3. Instalando o Python 3.12.7
Se você ainda não tem o Python 3.12.7 instalado, siga estas instruções:

Windows/OS

- a. Faça o download do Python 3.12.7 do [site oficial](https://www.python.org/downloads/release/python-3127/).
- b. Execute o instalador e marque a opção **"Add Python to PATH"**.
- c. Verifique se o Python foi instalado corretamente:

### 4. Verificando a versão instalada. Executando o comando abaixo

´
$ python --version
´

### 4. Configurando o Projeto no PyCharm
# Siga as instruções abaixo para configurar o projeto no **PyCharm**:
# Clonando o Repositório

- a. Primeiro, clone o repositório do GitHub para o seu ambiente local. 
No terminal do PyCharm ou na linha de comando, execute:

'''
git clone https://github.com/sainclersilva/ml-feature-store-api.git/
'''

- b. Navegue até o diretorio do projeto

'''
cd <caminho do projeto clonado>
'''

### 5. Abrindo o Projeto no PyCharm

- a. Abra o PyCharm.
- b. No menu inicial, clique em File > Open.
- c. Navegue até o diretório do projeto que você clonou e clique em OK.

### 6. Criando um Ambiente Virtual no PyCharm

- a. No PyCharm, abra o Settings (Ctrl+Alt+S ou Cmd+, no Mac).
- b. Navegue até Project: nome-do-projeto > Python Interpreter.
- c. No canto superior direito, clique no ícone de engrenagem e selecione Add > Virtualenv Environment.
- d. Escolha New environment e clique em OK para criar o ambiente virtual.


### 7. Instalando as Dependências
# Isso instalará todas as bibliotecas necessárias para o projeto.

- a. Após a criação do ambiente virtual, as dependências do projeto podem ser instaladas a partir do arquivo requirements.txt:
- b. No PyCharm, abra o terminal integrado (Alt+F12 ou Cmd+Option+T no Mac).
- c. No terminal, execute o comando:

'''
pip install -r requirements.txt
'''

- Os paths serao mapeados automaticamente através da lib pathlib do Python

### 8. Executando o projeto

- a. Para iniciar o projeto e acessar o notebook através da interface do jupter,
execute o comando abaixo no terminal integrado ao PyCharm

'''
jupyter notebook
'''

- b. Acesse o link gerado após execução do comando
- c. Depois acesso o arquivo feast_step.ipynb (http://localhost:8888/notebooks/feast_step.ipynb)
- d. Agora é só executar cada comando do notebook para ver os resultados

### 9. Executar API - FastAPI e Documentação Swagger

- a.Execute o comando abaixo no terminal integrado do PyCharm
  (certique-se de estar no diretorio <api> do projeto, onde se encontra o arquivo main.py da API)

'''
uvicorn main:app --reload --port 8080
'''

- b.Acesse a documentacao Swagger da API no navegador em: http://127.0.0.1:8080/docs
- c.Pode-se interagir com a API atraves da interface do link anterior.