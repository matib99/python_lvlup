from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Patient(BaseModel):
    name: str
    surename: str

app.id = -1

@app.get("/")
def root():
    return {"message": "Hello World during the coronavirus pandemic!"}

@app.post("/patient")
def patient(patient: Patient):
    app.id += 1
    return {"id": (app.id), "patient": patient}

@app.get("/method")
def method_get():
    return {"method": "GET"}

@app.post("/method")
def method_post():
    return {"method": "POST"}

@app.put("/method")
def method_put():
    return {"method": "PUT"}

@app.delete("/method")
def method_del():
    return {"method": "DELETE"}


