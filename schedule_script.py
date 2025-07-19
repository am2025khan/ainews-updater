
import schedule
import time
from news_fetcher import get_ai_news, save_news

def job():
    news = get_ai_news()
    save_news(news)

schedule.every(4).hours.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
