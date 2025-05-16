def find_hot_comics(news_articles, comics):
    hot_comics = []
    for comic in comics:
        title = comic.get("name", "").lower()
        for article in news_articles:
            headline = article.get("title", "").lower()
            if title in headline:
                hot_comics.append((comic, article))
                break
    return hot_comics
