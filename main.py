from fastapi import FastAPI, HTTPException, Request, Response, status
from pydantic import BaseModel

app = FastAPI()

class Patient(BaseModel):
    name: str
    surename: str
app.countRoot = 0
app.countWelc = 0
app.patients = []

@app.get("/")
def root():
    app.countRoot += 1
    return {"message": "Hello World during the coronavirus pandemic!",
            "counter": app.countRoot}

@app.get("/welcome")
def welcome():
    app.countWelc += 1
    return {"message": "Siema siema o tej porze każdy wypićmoże\n jakby nie było jest bardzo miło!",
            "counter": app.countWelc}
    

@app.post("/patient")
def patient(patient: Patient):
    app.patients.append(patient)
    return {"id": (len(app.patients) - 1), "patient": patient}

@app.get("/patient/{pk}", response_model=Patient)
def patient(pk: int):
    if pk >= len(app.patients) or pk < 0:
        raise HTTPException(status_code=204, detail="Patient not found")
    return app.patients[pk]

@app.api_route(path="/method", methods=["GET", "POST", "DELETE", "PUT", "OPTIONS"])
def read_request(request: Request):
    return {"method": request.method}

@app.get("/clear")
def method_del():
    app.patients.clear()
    return {"ok": "OK"}


