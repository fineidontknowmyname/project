from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"status":"alive"}

@app.post("/evaluate")
def evaluate(data: dict):
    return {"result": 42}    