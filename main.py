from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
import requests

app = FastAPI()

# ✅ Uses only required fields to avoid 400 errors
REST_COUNTRIES_URL = "https://restcountries.com/v3.1/all?fields=name,capital,population,region"


@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Country Info API 🚀. Try /api/countries or /docs for Swagger UI."
    }


@app.get("/api/countries")
def get_countries(name: str = Query(None), sort: str = Query(None)):
    try:
        response = requests.get(REST_COUNTRIES_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"ERROR fetching from REST API: {e}")
        raise HTTPException(status_code=503, detail="Failed to fetch data from REST Countries API.")

    simplified = []

    for country in data:
        name_data = country.get("name", {})
        name_val = name_data.get("common", "Unknown")

        capital = country.get("capital", [])
        capital_val = capital[0] if capital else "N/A"

        population = country.get("population", 0)
        region = country.get("region", "Unknown")

        simplified.append({
            "name": name_val,
            "capital": capital_val,
            "population": population,
            "region": region
        })

    # 🔍 Filter by name if provided
    if name:
        simplified = [
            c for c in simplified if name.lower() in c["name"].lower()
        ]

    # 🔢 Sort by population if requested
    if sort == "asc":
        simplified.sort(key=lambda x: x["population"])
    elif sort == "desc":
        simplified.sort(key=lambda x: x["population"], reverse=True)

    return JSONResponse(content=simplified)