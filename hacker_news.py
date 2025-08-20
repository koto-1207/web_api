import requests
import time


# トップ記事のIDを取得
def get_top_news_ids(limit=30):
    url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    try:
        top_ids = requests.get(url, timeout=5).json()[:limit]
        return top_ids
    except requests.RequestException as e:
        print("Error fetiching top stories:", e)
        return []


# 記事情報を取得
def get_story_id(story_id):
    url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    try:
        text = requests.get(url, timeout=5).json()
        return text
    except requests.RequestException as e:
        print(f"Error fetiching story {story_id}:", e)
        return {}


# 記事を表示
def display_story(story):
    title = story.get("title")
    link = story.get("url", "")
    if title:
        print({"title": title, "link": link})


def main():
    top_ids = get_top_news_ids()
    for story_id in top_ids:
        story = get_story_id(story_id)
        display_story(story)
        time.sleep(1)


if __name__ == "__main__":
    main()
