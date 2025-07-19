
import requests
import json

def get_ai_news():
    url = "https://newsapi.org/v2/everything"
    params = {
        'q': "artificial intelligence",
        'language': 'en',
        'sortBy': 'publishedAt',
        'apiKey': "YOUR_NEWSAPI_KEY"
    }
    response = requests.get(url, params=params)
    articles = response.json().get("articles", [])
    return articles[:10]

def save_news(news, filename="news.json"):
    with open(filename, "w") as f:
        json.dump(news, f)
