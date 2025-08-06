# 🌍 Country Information API

This is a simple backend API built with **FastAPI** that fetches and serves country information from the public [REST Countries API](https://restcountries.com/).

It supports:
- ✅ Fetching country name, capital, population, and region
- 🔍 Filtering by name (`?name=`)
- 🔢 Sorting by population (`?sort=asc|desc`)
- ⚠️ Graceful error handling

## 📦 Tech Stack

- **Python 3.10+**
- **FastAPI** (web framework)
- **Uvicorn** (ASGI server)
- **Requests** (to fetch external API)

## 🚀 How to Run

### 1. Clone or download the project

```bash
git clone <your_repo_url>
cd country_api
```

### 2. Create and activate virtual environment (optional)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the server

```bash
python3 -m uvicorn main:app --reload
```

> Default server runs at: `http://127.0.0.1:8000`

## 🌐 API Endpoints

### `GET /`

Basic root route.

#### Response:
```json
{
  "message": "Welcome to the Country Info API 🚀. Try /api/countries or /docs for Swagger UI."
}
```

### `GET /api/countries`

Fetches country data from the REST Countries API and returns a simplified JSON response.

### ✅ Query Parameters

| Param  | Type   | Description                                       |
|--------|--------|---------------------------------------------------|
| name   | string | (optional) Filter countries by name (case-insensitive) |
| sort   | string | (optional) `asc` or `desc` — sort by population   |

### 🔍 Examples

- `GET /api/countries`
- `GET /api/countries?name=united`
- `GET /api/countries?name=united&sort=desc`

## 🧪 Swagger API Docs

Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## ✅ Example Response

```json
[
  {
    "name": "United States",
    "capital": "Washington, D.C.",
    "population": 331893745,
    "region": "Americas"
  },
  {
    "name": "United Kingdom",
    "capital": "London",
    "population": 67215293,
    "region": "Europe"
  }
]
```

## ❗ Error Handling

| Status Code | Reason |
|-------------|--------|
| 503 | REST Countries API is down or not responding |
| 200 + `[]` | Filter returned no matching results |

## ✨ Bonus Ideas

Want to level up the project? Consider adding:
- 🧠 In-memory caching
- ✅ Unit tests using `pytest`
- 🐳 Docker support
- 📁 GitHub Actions for CI/CD

