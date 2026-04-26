from fastapi import FastAPI, Response
from pydantic import BaseModel
from prometheus_client import Counter, generate_latest

REQUEST_COUNT = Counter('request_count', 'Total Requests')

class LoginRequest(BaseModel):
    username: str
    password: str

app = FastAPI()

@app.get("/")
def home():
    REQUEST_COUNT.inc()
    return {"message": "Welcome to DevSecOps Project"}

@app.get("/health")
def health():
    REQUEST_COUNT.inc()
    return {"status": "ok"}

@app.post("/login")
def login(request: LoginRequest):
    REQUEST_COUNT.inc()
    if request.username == "admin" and request.password == "1234":
        return {"message": "Login successful"}
    else:
        return {"message": "Invalid credentials"}

@app.get("/data")
def get_data():
    REQUEST_COUNT.inc()
    return {"items": ["server1", "server2"]}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")
