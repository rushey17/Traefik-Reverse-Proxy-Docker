from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def read_root():
    return {"Hello": "World"}

@app.get("/api/users/list")
def read_users():
    return {"users": [{"username": "alice"}, {"username": "bob"}]}

@app.get("/api/names")
def read_names():
    return {"names": ["Alice", "Bob"]}

@app.get("/api/employees")
def get_employees(department: str, limit: int = 10):
    return {"department": department, "limit": limit}
