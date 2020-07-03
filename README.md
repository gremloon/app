# Template app 

### Build on streamlit and awesome-streamlit as helper package

### Roadmap
- Connect to DBs and Backend
- Deploy through Jupyterhub
- Auth
- Implement upcoming release

### Run local (if you only want to run it, choose Docker install)
```
git clone https://github.com/gremloon/app.git  
cd app  
```

Create a virtualenvironment (Python >3.7):
```
python -m venv .app  
conda create -n app python=3.7.4  
virtualenv .app  

```

Activate Virtual Environment
```
source .app/Scripts/activate
activate awesome-streamlit
source .app/bin/activate
```

Install
```
pip install -r requirements.txt  
streamline run app.py  
Access via localhost:8501  
```

### Run via Docker
```
git clone https://github.com/gremloon/app.git  
cd app  
docker build -t gremloon/app .
docker run -i -p '8501:8501' gremloon/app:latest 
Access via localhost:8501  
```
