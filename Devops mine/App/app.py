from fastapi import FastAPI
from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to DevSecOps Project"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/login")
def login(request: LoginRequest):
    if request.username == "admin" and request.password == "1234":
        return {"message": "Login successful"}
    else:
        return {"message": "Invalid credentials"}

@app.get("/data")
def get_data():
    return {"items": ["server1", "server2"]}
