import streamlit as st
from comicvine import search_comics, get_comic_details
from news_signals import fetch_newsapi_articles, fetch_google_news_rss
from predictor import find_hot_comics
from PIL import Image
import requests
from io import BytesIO

st.set_page_config(page_title="Comic Buy-Now Predictor", layout="wide", initial_sidebar_state="expanded")

# Comic-style CSS
st.markdown("""
    <style>
    body { background-color: #181818; color: #f8f8f2; }
    .stApp { background-color: #181818; }
    .comic-card {
        background: #23272f;
        border: 3px solid #ffcc00;
        border-radius: 12px;
        box-shadow: 0 0 12px #ffcc00;
        padding: 1em;
        margin-bottom: 1em;
    }
    .hot-badge {
        background: #ff3131;
        color: #fff;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.2em 0.6em;
        margin-left: 0.5em;
        font-size: 1.1em;
        box-shadow: 0 0 8px #ff3131;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🦸‍♂️ Comic Buy-Now Predictor")
st.markdown("#### Find the next hot comic before the price spikes! _(Dark, comic-style dashboard)_")

search_query = st.text_input("🔎 Search for any comic book (title, character, or issue):", "")

if search_query:
    with st.spinner("Searching ComicVine..."):
        comics = search_comics(search_query, limit=10)
    st.subheader("Search Results")
    for comic in comics:
        st.markdown(f"<div class='comic-card'>", unsafe_allow_html=True)
        st.markdown(f"**{comic.get('name', 'Unknown Title')}**")
        if comic.get("image") and comic["image"].get("small_url"):
            img_url = comic["image"]["small_url"]
            response = requests.get(img_url)
            img = Image.open(BytesIO(response.content))
            st.image(img, width=120)
        st.markdown(f"Type: {comic.get('resource_type', 'N/A')}")
        st.markdown(f"Publisher: {comic.get('publisher', {}).get('name', 'N/A')}")
        st.markdown(f"<a href='{comic.get('site_detail_url', '#')}' target='_blank'>More Info</a>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # News signals
    with st.spinner("Fetching news signals..."):
        newsapi_articles = fetch_newsapi_articles(search_query, page_size=10)
        rss_articles = fetch_google_news_rss(search_query, num_articles=5)
        all_articles = newsapi_articles + [{"title": entry.title, "link": entry.link, "publishedAt": entry.published} for entry in rss_articles]

    st.subheader("News Feed")
    for article in all_articles:
        st.markdown(f"**[{article.get('title')}]({article.get('url', article.get('link', '#'))})**")
        st.markdown(f"Published: {article.get('publishedAt', '')}")

    # Hot comics
    hot_comics = find_hot_comics(all_articles, comics)
    if hot_comics:
        st.subheader("🔥 Hot Comics (Likely to Increase in Value)")
        for comic, article in hot_comics:
            st.markdown(f"<div class='comic-card'>", unsafe_allow_html=True)
            st.markdown(f"**{comic.get('name', 'Unknown Title')}** <span class='hot-badge'>HOT!</span>", unsafe_allow_html=True)
            if comic.get("image") and comic["image"].get("small_url"):
                img_url = comic["image"]["small_url"]
                response = requests.get(img_url)
                img = Image.open(BytesIO(response.content))
                st.image(img, width=120)
            st.markdown(f"Type: {comic.get('resource_type', 'N/A')}")
            st.markdown(f"Publisher: {comic.get('publisher', {}).get('name', 'N/A')}")
            st.markdown(f"<a href='{comic.get('site_detail_url', '#')}' target='_blank'>More Info</a>", unsafe_allow_html=True)
            st.markdown(f"**Related News:** [{article.get('title')}]({article.get('url', article.get('link', '#'))})", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info("No hot comics found for this search yet. Try another title or check back soon!")

else:
    st.info("Enter a search term to get started!")

