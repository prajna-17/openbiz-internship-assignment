
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_valid_submission():
    response = client.post("/submit", json={
        "aadhaar": "123456789012",
        "pan": "ABCDE1234F",
        "pincode": "110001",
        "state": "Delhi",
        "city": "New Delhi"
    })
    assert response.status_code == 200

def test_invalid_aadhaar():
    response = client.post("/submit", json={
        "aadhaar": "123",
        "pan": "ABCDE1234F"
    })
    assert response.status_code == 400

def test_invalid_pan():
    response = client.post("/submit", json={
        "aadhaar": "123456789012",
        "pan": "12345"
    })
    assert response.status_code == 400
