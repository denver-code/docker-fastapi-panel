# Docker FastAPI Panel  
Demo reposiroty that has basic docker + fastapi integration.  
In future will be used in some of my projects

## Features  
- Show containers + their status
- Start container
- Stop Container

## Download  
```bash
git clone https://github.com/denver-code/docker-fastapi-panel
cd docker-fastapi-panel
```

# Make sure docker engine already running!

## Docker Compose
Note that current method requires to completly expose the docker socket (eg `/var/run/docker.sock:/var/run/docker.sock`)  
This is dangerous way of doing things, but stil WIP to figure out more secure ways  
```bash
docker compose up -d
```  
Add `sudo` if required  

## Manual
```bash
poetry install
poetry shell
uvicorn main:app
```  
or  
```bash
pip install uvicorn docker fastapi
uvicorn main:app
```

# Available routes  
`GET /containers` - returns 
`POST /stop/ID` - stops container
`POST /start/ID` - starts container