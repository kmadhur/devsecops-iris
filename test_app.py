from fastapi.testclient import TestClient
from main import app

# test to check the correct functioning of the /ping route
def test_ping():
    with TestClient(app) as client:
        response = client.get("/ping")
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"ping": "pong"}


# test to check if Iris Virginica is classified correctly
def test_pred_virginica():
    # defining a sample payload for the testcase
    payload = {
        "sepal_length": 3.3,
        "sepal_width": 4.8,
        "petal_length": 3.0,
        "petal_width": 5.1,
    }
    with TestClient(app) as client:
        response = client.post("/predict_flower", json=payload)
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"flower_class": "Iris Virginica"}

# test to check feedback_loop
def test_feedback_loop():
    # defining a sample payload for the testcase
    payload = [{
        "sepal_length": 3.3,
        "sepal_width": 4.8,
        "petal_length": 3.0,
        "petal_width": 5.1,
		"flower_class":"Iris Virginica"
    }]
    with TestClient(app) as client:
        response = client.post("/feedback_loop", json=payload)
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"detail": "Feedback loop successful"}
