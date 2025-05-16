# Comic Buy-Now Predictor

A comic-style, dark-themed dashboard to help you (and Andy!) spot the next hot comic before prices spike.

## Features

- Search any comic book (title, character, or issue)
- See news signals from NewsAPI.org and Google News RSS
- "Hot" indicator for comics likely to increase in value
- Comic-inspired dark theme
- Public link (deploy to Streamlit Cloud)

## Setup

1. Clone/download this repo.
2. Install dependencies:
3. Add your API keys in `comicvine.py` and `news_signals.py` (already set for you).
4. Run locally:

streamlit run app.py

5. Deploy to [Streamlit Cloud](https://streamlit.io/cloud) for a public link.

## Customization

- To change the theme or add more features, edit `app.py`.
- To add price tracking, extend `predictor.py` and the dashboard.

---

Enjoy, and let me know if you want more features!