import requests
import feedparser

NEWSAPI_KEY = "58024358b9824450ac6ab37ee13c540e"

def fetch_newsapi_articles(query, page_size=10):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "apiKey": NEWSAPI_KEY,
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": page_size,
    }
    resp = requests.get(url, params=params)
    data = resp.json()
    return data.get("articles", [])

def fetch_google_news_rss(query, num_articles=10):
    feed_url = f"https://news.google.com/rss/search?q={query}+comic+book+adaptation"
    feed = feedparser.parse(feed_url)
    return feed.entries[:num_articles]
