from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Patient(BaseModel):
    name: str
    surename: str

app.patients = []

@app.get("/")
def root():
    return {"message": "Hello World during the coronavirus pandemic!"}

@app.post("/patient")
def patient(patient: Patient):
    app.patients.append(patient)
    return {"id": (len(app.patients) - 1), "patient": patient}

@app.get("/patient/{pk}", response_model=Patient)
def patient(pk: int):
    if pk >= len(app.patients) or pk < 0:
        raise HTTPException(status_code=204, detail="Patient not found")
    return app.patients[pk]

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

@app.get("/clear")
def method_del():
    app.patients.clear()
    return {"ok": "OK"}


