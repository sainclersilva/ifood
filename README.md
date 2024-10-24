### 1. Project Information
Feature Store Project - FastAPI

### 2. System Requirements
Python 3.12.7: Make sure you have Python 3.12.7 installed.
pip: Python package installer (usually comes with Python installation).
Virtualenv: (Optional, but recommended) to isolate dependencies.
PyCharm 2024.2.3 (recommended IDE) or VSCode.

### 3. Installing Python 3.12.7
If you don't have Python 3.12.7 installed yet, follow these instructions:

Windows/OS

a. Download Python 3.12.7 from the official site.
b. Run the installer and check the "Add Python to PATH" option.
c. Verify that Python was installed correctly:

### 4. Checking the Installed Version. Run the command below

`
$ python --version
`

### 5. Setting Up the Project in PyCharm
Follow the instructions below to set up the project in PyCharm: Cloning the Repository

a. First, clone the GitHub repository to your local environment. In PyCharm's terminal or the command line, run:
git clone https://github.com/sainclersilva/ifood.git/

b. Navigate to the project directory:

`
cd <path to the cloned project>
`

### 6. Opening the Project in PyCharm

a. Open PyCharm.
b. In the startup menu, click File > Open.
c. Navigate to the directory of the project you cloned and click OK.

### 7. Creating a Virtual Environment in PyCharm

a. In PyCharm, open Settings (Ctrl+Alt+S or Cmd+, on Mac).
b. Navigate to Project: project-name > Python Interpreter.
c. In the top right corner, click the gear icon and select Add > Virtualenv Environment.
d. Choose New environment and click OK to create the virtual environment.
8. Installing Dependencies

This will install all the necessary libraries for the project.

a. After creating the virtual environment, the project dependencies can be installed from the requirements.txt file:
b. In PyCharm, open the integrated terminal (Alt+F12 or Cmd+Option+T on Mac).
c. In the terminal, run the command:

`
pip install -r requirements.txt
`

Paths will be automatically mapped through Python's pathlib library.

### 9. Running the Project

a. To start the project and access the notebook via the Jupyter interface, run the following command in PyCharm's integrated terminal:

`
jupyter notebook
`

b. Access the link generated after running the command.
c. Then open the file feast_step.ipynb (http://localhost:8888/notebooks/feast_step.ipynb).
d. Now, just execute each command in the notebook to see the results.

### 10. Running the API - FastAPI and Swagger Documentation

a. Run the following command in PyCharm's integrated terminal (make sure you are in the <api> directory of the project, where the API's main.py file is located):

`
uvicorn main:app --reload --port 8080
`

b. Access the Swagger API documentation in the browser at: http://127.0.0.1:8080/docs
c. You can interact with the API through the interface at the previous link.

-----------------------------------------------------------------------

### 1. Informções do projeto
Feature Store Project - FastAPI

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

`
$ python --version
`

### 5. Configurando o Projeto no PyCharm
Siga as instruções abaixo para configurar o projeto no **PyCharm**:
Clonando o Repositório

- a. Primeiro, clone o repositório do GitHub para o seu ambiente local. 
No terminal do PyCharm ou na linha de comando, execute:

`
git clone https://github.com/sainclersilva/ifood.git/
`

- b. Navegue até o diretório do projeto

`
cd <caminho do projeto clonado>
`

### 6. Abrindo o Projeto no PyCharm

- a. Abra o PyCharm.
- b. No menu inicial, clique em File > Open.
- c. Navegue até o diretório do projeto que você clonou e clique em OK.

### 7. Criando um Ambiente Virtual no PyCharm

- a. No PyCharm, abra o Settings (Ctrl+Alt+S ou Cmd+, no Mac).
- b. Navegue até Project: nome-do-projeto > Python Interpreter.
- c. No canto superior direito, clique no ícone de engrenagem e selecione Add > Virtualenv Environment.
- d. Escolha New environment e clique em OK para criar o ambiente virtual.


### 8. Instalando as Dependências
Isso instalará todas as bibliotecas necessárias para o projeto.

- a. Após a criação do ambiente virtual, as dependências do projeto podem ser instaladas a partir do arquivo requirements.txt:
- b. No PyCharm, abra o terminal integrado (Alt+F12 ou Cmd+Option+T no Mac).
- c. No terminal, execute o comando:

`
pip install -r requirements.txt
`

- Os paths serão mapeados automaticamente através da lib pathlib do Python

### 9. Executando o projeto

- a. Para iniciar o projeto e acessar o notebook através da interface do jupter,
execute o comando abaixo no terminal integrado ao PyCharm

`
jupyter notebook
`

- b. Acesse o link gerado após execução do comando
- c. Depois acesso o arquivo feast_step.ipynb (http://localhost:8888/notebooks/feast_step.ipynb)
- d. Agora é só executar cada comando do notebook para ver os resultados

### 10. Executar API - FastAPI e Documentação Swagger

- a.Execute o comando abaixo no terminal integrado do PyCharm
  (certique-se de estar no diretorio <api> do projeto, onde se encontra o arquivo main.py da API)

`
uvicorn main:app --reload --port 8080
`

- b.Acesse a documentacao Swagger da API no navegador em: http://127.0.0.1:8080/docs
- c.Pode-se interagir com a API através da interface do link anterior.

### - ###