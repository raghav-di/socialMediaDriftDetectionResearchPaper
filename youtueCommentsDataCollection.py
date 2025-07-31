from googleapiclient.discovery import build
import pandas as pd
import time
from datetime import datetime

# Your API key
api_key = "#####################################"
youtube = build("youtube", "v3", developerKey=api_key)

# Your topic queries
queries = [
    "morning routine", "daily expenses", "monthly budget", "rent increase", "grocery prices",
    "commute stress", "work-life balance", "remote work", "office politics", "job satisfaction",
    "career change", "freelancing", "side hustle", "student debt", "exam stress",
    "parenting tips", "childcare cost", "relationship advice", "breakup", "dating apps",
    "meal planning", "cheap recipes", "cooking hacks", "healthy eating", "food inflation",
    "travel plans", "solo travel", "flight delays", "hotel reviews", "packing tips",
    "home renovation", "DIY projects", "minimalist living", "decluttering", "moving out",
    "fitness goals", "weight loss", "running motivation", "gym anxiety", "healthy habits",
    "mental health", "therapy", "anxiety triggers", "depression", "self-care",
    "confession", "venting", "life regrets", "personal growth", "changing habits",
    "learning new skills", "online courses", "productivity hacks", "time management", "focus issues",
    "phone addiction", "screen time", "tech burnout", "app recommendations", "digital detox",
    "local news", "political views", "climate anxiety", "social justice", "urban life",
    "book recommendations", "reading habits", "journaling", "creative writing", "bullet journaling",
    "fashion trends", "skincare routine", "body image", "confidence", "style tips",
    "pet care", "dog behavior", "cat memes", "animal rescue", "funny pets",
    "gaming addiction", "game reviews", "console wars", "multiplayer toxicity", "game updates",
    "movie reviews", "TV binge", "Netflix shows", "true crime", "documentary tips",
    "music taste", "playlist sharing", "concert experience", "headphone reviews", "audiophile tips",
    "eco-friendly", "zero waste", "climate change", "sustainable living", "green habits"
]

# Output storage
comments_data = []
total_comments = 0
MAX_COMMENTS = 100

def search_videos(query):
    video_ids = set()
    next_page_token = None
    while len(video_ids) < 100:  # You can raise this limit per query
        try:
            response = youtube.search().list(
                q=query,
                part="id",
                type="video",
                publishedAfter="2018-01-01T00:00:00Z",
                publishedBefore="2025-12-31T23:59:59Z",
                maxResults=50,
                pageToken=next_page_token
            ).execute()
        except Exception as e:
            print("Search error:", e)
            break

        for item in response.get("items", []):
            video_ids.add(item["id"]["videoId"])

        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break
        time.sleep(0.2)

    return list(video_ids)

def get_comments(video_id, query):
    global total_comments
    next_page_token = None

    while True:
        if total_comments >= MAX_COMMENTS:
            return

        try:
            response = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                maxResults=100,
                pageToken=next_page_token,
                textFormat="plainText"
            ).execute()
        except Exception as e:
            if "disabled comments" in str(e):
                break
            print("Comment error:", e)
            break

        for item in response.get("items", []):
            snippet = item["snippet"]["topLevelComment"]["snippet"]
            comments_data.append({
                "query": query,
                "videoId": video_id,
                "comment": snippet.get("textDisplay", ""),
                "author": snippet.get("authorDisplayName", ""),
                "publishedAt": snippet.get("publishedAt", ""),
                "likeCount": snippet.get("likeCount", 0)
            })
            total_comments += 1

        next_page_token = response.get("nextPageToken")
        if not next_page_token or total_comments >= MAX_COMMENTS:
            break
        time.sleep(0.1)

# Main loop
for query in queries:
    print(f"\n🔍 Searching for videos on: {query}")
    video_ids = search_videos(query)
    print(f"Found {len(video_ids)} videos.")
    for video_id in video_ids:
        if total_comments >= MAX_COMMENTS:
            break
        get_comments(video_id, query)
        print(f"Total comments so far: {total_comments}")
        time.sleep(0.2)
    if total_comments >= MAX_COMMENTS:
        break

# Save to CSV
df = pd.DataFrame(comments_data)
df["publishedAt"] = pd.to_datetime(df["publishedAt"])
df = df[df["publishedAt"].dt.year.between(2018, 2025)]  # optional post-filter
df.to_csv("youtube_comments.csv", index=False)
print("\n✅ Done. Saved to youtube_1M_comments.csv")
