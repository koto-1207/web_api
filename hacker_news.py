import requests
import time


def get_top_news(limit=30):
    news_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    top_ids = requests.get(news_url).json()[:limit]

    for news_id in top_ids:
        text_url = f"https://hacker-news.firebaseio.com/v0/item/{news_id}.json"
        text = requests.get(text_url, timeout=5).json()

        title = text.get("title")
        link = text.get("url")

        print({"title": title, "link": link})

        time.sleep(1)


def main():
    get_top_news()


if __name__ == "__main__":
    main()
