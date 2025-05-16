import requests

COMICVINE_API_KEY = "f36334051b3c34e5a2237b26eb33aa8a75d46817"
BASE_URL = "https://comicvine.gamespot.com/api"

def search_comics(query, limit=10):
    url = f"{BASE_URL}/search/"
    params = {
        "api_key": COMICVINE_API_KEY,
        "format": "json",
        "resources": "issue,volume",
        "query": query,
        "limit": limit,
    }
    resp = requests.get(url, params=params)
    data = resp.json()
    return data.get("results", [])

def get_comic_details(comic_id, resource_type="issue"):
    url = f"{BASE_URL}/{resource_type}/4000-{comic_id}/"
    params = {
        "api_key": COMICVINE_API_KEY,
        "format": "json",
    }
    resp = requests.get(url, params=params)
    return resp.json().get("results", {})
