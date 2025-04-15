from fastapi import FastAPI
import docker


app = FastAPI()
client = docker.from_env()


@app.get("/containers")
def list_containers():
    return [
        f"{container.name} - {container.status}"
        for container in client.containers.list()
    ]


@app.post("/start/{container_name}")
def start_container(container_name: str):
    container = client.containers.get(container_name)
    container.start()
    return {"status": f"{container_name} started"}

@app.post("/stop/{container_name}")
def stop_container(container_name: str):
    container = client.containers.get(container_name)
    container.stop()
    return {"status": f"{container_name} stopped"}