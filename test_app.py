from app import app, greet
 
client = app.test_client()
 
 
def test_greet():
    assert greet("Ravi") == "Hello, Ravi!"
 
 
def test_home():
    response = client.get("/")
    assert response.status_code == 200
 
 
def test_health():
    response = client.get("/health")
    assert response.get_json()["status"] == "ok"
