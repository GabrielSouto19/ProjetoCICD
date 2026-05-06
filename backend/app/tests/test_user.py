from fastapi.testclient import TestClient
from app.main import app

def test_get_all_user():
    client = TestClient(app)# arrange --> montar o ambiente de testes
    response = client.get("/users")# act # agir 
    # assert garantir o argumento 
    assert response.status_code == 200# Garante que a resposta seja 200 OK
    assert response.json() == "Olá, Mundo!"# Garante que a resposta seja 200 OK

def test_register_user():
    client = TestClient(app)
    response = client.post("/users")

    assert response.status_code == 201
    assert response.json() == "cadastrei usuário"