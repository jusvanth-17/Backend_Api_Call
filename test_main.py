import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Welcome" in response.json()["message"]

def test_get_countries_success():
    response = client.get("/api/countries")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    if response.json():
        country = response.json()[0]
        assert "name" in country
        assert "capital" in country
        assert "population" in country
        assert "region" in country

def test_get_countries_with_filter():
    response = client.get("/api/countries?name=united")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    for country in response.json():
        assert "united" in country["name"].lower()

def test_get_countries_with_sort():
    response = client.get("/api/countries?sort=asc")
    assert response.status_code == 200
    data = response.json()
    assert data == sorted(data, key=lambda x: x["population"])

def test_get_countries_with_filter_and_sort():
    response = client.get("/api/countries?name=united&sort=desc")
    assert response.status_code == 200
    data = response.json()
    assert all("united" in c["name"].lower() for c in data)
    assert data == sorted(data, key=lambda x: x["population"], reverse=True)
