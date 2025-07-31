import praw
import pandas as pd
import datetime

# Your Reddit credentials here
reddit = praw.Reddit(
    client_id="##################################",
    client_secret="##################################",
    user_agent="##################################"
)

subreddits = [
    "AskReddit", "CasualConversation", "LifeProTips", "Frugal", "PersonalFinance",
    "Budget", "SimpleLiving", "GetMotivated", "selfimprovement", "productivity",
    "socialskills", "relationships", "dating", "Parenting", "Work",
    "jobs", "antiwork", "careeradvice", "college", "StudentLoans",
    "Cooking", "EatCheapAndHealthy", "BudgetFood", "MealPrepSunday", "FoodPorn",
    "travel", "solotravel", "backpacking", "HomeImprovement", "DIY",
    "Home", "ApartmentLiving", "InteriorDesign", "minimalism", "declutter",
    "Fitness", "loseit", "running", "bodyweightfitness", "HealthyFood",
    "mentalhealth", "depression", "Anxiety", "DecidingToBeBetter", "offmychest",
    "TrueOffMyChest", "confession", "Vent", "changemyview", "explainlikeimfive",
    "todayilearned", "Showerthoughts", "nostupidquestions", "IWantToLearn", "howto",
    "technology", "smartphones", "Android", "iPhone", "gadgets",
    "india", "Delhi", "mumbai", "bangalore", "kolkata",
    "news", "worldnews", "NotTheOnion", "UpliftingNews", "Futurology",
    "books", "writing", "journaling", "BulletJournal", "stationery",
    "fashion", "MaleFashionAdvice", "FemaleFashionAdvice", "SkincareAddiction", "ABraThatFits",
    "pets", "dogs", "cats", "aww", "AnimalsBeingBros",
    "gaming", "boardgames", "videogames", "NintendoSwitch", "PS5",
    "movies", "television", "NetflixBestOf", "Documentaries", "TrueCrime",
    "music", "listentothis", "spotify", "audiophile", "headphones",
    "environment", "sustainability", "ZeroWaste", "climate", "urbanplanning"
]


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



# Collect posts
posts = []
for sub in subreddits:
    for query in queries:
        print(f"Searching r/{sub} for '{query}'...")
        try:
          for submission in reddit.subreddit(sub).search(query, limit=2000):
              if not submission.stickied:
                  posts.append({
                      "id": submission.id,
                      "title": submission.title,
                      "text": submission.selftext,
                      "subreddit": sub,
                      "score": submission.score,
                      "created": datetime.datetime.utcfromtimestamp(submission.created_utc),
                      "url": submission.url,
                      "query": query
                  })
        except:
            print(f"Error collecting posts from r/{sub}")

# Save
df = pd.DataFrame(posts).drop_duplicates(subset="id")
df.to_csv("multi_subreddit_query_reddit_data_original.csv", index=False)
print(f"✅ Saved {len(df)} posts to CSV")
