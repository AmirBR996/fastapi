import json
from fastapi import FastAPI
app = FastAPI()
def info():
    with open("patients.json" , "r") as f:
        data = json.load(f)
    return data
@app.get("/")
def hello():
    return {"message" : "This is pathient API"}
@app.get("/about")
def get():
    return {"message" : "This is about patient data"}

@app.get("/data")
def data():
    data = info()
    return data