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

## 📄 License

This project is for educational and assessment use.


---

## 🧠 In-Memory Caching

The API uses an in-memory cache to avoid repeatedly calling the public REST Countries API.

- Data is fetched once and cached for **5 minutes (300 seconds)**
- Subsequent requests within this time return cached data
- This improves performance and reduces external API dependency

> Cache logic is implemented inside the `fetch_countries()` function and uses a simple dictionary to store the data and timestamp.

---

## 🧪 Running Unit Tests

This project includes basic unit tests using `pytest` and FastAPI’s `TestClient`.

### ✅ How to Run Tests:

1. Make sure `pytest` is installed:
```bash
pip install pytest
```

2. Run the test suite:
```bash
pytest test_main.py
```

### 🔬 Tests Covered:

| Test | Description |
|------|-------------|
| `test_root()` | Ensures welcome message is returned on `/` |
| `test_get_countries_success()` | Validates country list is returned |
| `test_get_countries_with_filter()` | Checks name-based filtering |
| `test_get_countries_with_sort()` | Verifies population sorting |
| `test_get_countries_with_filter_and_sort()` | Confirms filtering + sorting works together |
