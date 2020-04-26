from fastapi import FastAPI, HTTPException, Request, Depends, Cookie, Response, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from hashlib import sha256

import secrets

app = FastAPI()

app.secret_key = "very constant and random secret, best sixty four (64) characters"
app.tokens_list = []
security = HTTPBasic()

class Patient(BaseModel):
    name: str
    surename: str
app.countRoot = 0
app.countWelc = 0
app.patients = []

def log_in_and_get_token(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "trudnY")
    correct_password = secrets.compare_digest(credentials.password, "PaC13Nt")
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    token = sha256(bytes(f"{credentials.username}{credentials.password}{app.secret_key}", encoding='utf8')).hexdigest()
    app.tokens_list.append(token)
    return token


@app.get("/")
def root():
    app.countRoot += 1
    return {"message": "Hello World during the coronavirus pandemic!",
            "counter": app.countRoot}

@app.get("/welcome")
def welcome():
    app.countWelc += 1
    return {"message": "Welcome!",
            "counter": app.countWelc}
    

@app.post("/patient")
def new_patient(patient: Patient):
    app.patients.append(patient)
    return {"id": (len(app.patients) - 1), "patient": patient}

@app.get("/patient/{pk}", response_model=Patient)
def get_patient(pk: int):
    if pk >= len(app.patients) or pk < 0:
        raise HTTPException(status_code=204, detail="Patient not found")
    return app.patients[pk]

# @app.api_route(path="/method", methods=["GET", "POST", "DELETE", "PUT", "OPTIONS"])
# def read_request(request: Request):
#     return {"method": request.method}

@app.post("/login")
def login(request: Request, credentials_user = Depends(log_in_and_get_token)):
    printf(credentials_user)
    response = RedirectResponse(url = "/welcome")
    response.status_code = status.HTTP_302_FOUND
    return response


@app.get("/clear")
def method_del():
    app.patients.clear()
    return {"ok": "OK"}


