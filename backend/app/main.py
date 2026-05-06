from datetime import datetime

from fastapi import Depends, FastAPI, Response

app = FastAPI()


@app.get("/users")
def get_all_users():
    datetime.now()
    return "Olá, Mundo!"

@app.post("/users",status_code=201)
def register_user():
    datetime.now()
    return "cadastrei usuário"
