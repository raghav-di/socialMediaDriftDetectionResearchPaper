import pandas as pd
import matplotlib.pyplot as plt

queryfilter = [
    # # World / World Issues
    # "global conflicts",
    # "international relations",
    # "human rights issues",
    # "refugee crisis",
    # "geopolitical tensions",
    # "world economy trends",
    # "climate migration",
    # "global inequality",
    # "UN peacekeeping",
    # "border disputes",
    # # Environment & Sustainability
    # "climate change solutions",
    # "renewable energy innovations",
    # "plastic pollution cleanup",
    # "sustainable agriculture",
    # "carbon footprint reduction",
    # "green technology",
    # "deforestation impact",
    # "ocean conservation",
    # "zero waste lifestyle",
    # "biodiversity protection",
    # # Life & Personal Growth
    # "self improvement tips",
    # "goal setting strategies",
    # "mindfulness practices",
    # "time management hacks",
    # "overcoming procrastination",
    # "building confidence",
    # "emotional intelligence",
    # "habit formation",
    # "resilience training",
    # "life coaching advice",
    # Health & Mental Well-being
    "mental health awareness",
    "stress management techniques",
    "anxiety coping strategies",
    "depression recovery stories",
    "therapy benefits",
    "meditation for mental health",
    "work-life balance",
    "nutrition and mental health",
    "sleep hygiene tips",
    "exercise for mental well-being"
]
querytrendy = dfy[dfy['query'].isin(queryfilter)]
# queryfilter = ["local news", "political views", "climate anxiety", "social justice", "urban life"]
# queryfilter = ["eco-friendly", "zero waste", "climate change", "sustainable living", "green habits"]
# queryfilter = ["life regrets", "personal growth", "changing habits", "healthy habits", "body image"]
queryfilter = ["mental health", "therapy", "anxiety triggers", "depression", "self-care"]
querytrendr = dfr[dfr['query'].isin(queryfilter)]

# Ensure 'created' is in datetime format
querytrendr["created"] = pd.to_datetime(querytrendr["created"], errors="coerce")
querytrendy["created"] = pd.to_datetime(querytrendy["created"], errors="coerce")

# Extract the year
querytrendr["year"] = querytrendr["created"].dt.year
querytrendy["year"] = querytrendy["created"].dt.year
querytrendy = querytrendy[querytrendy['year']>=2018]

# Filter only relevant years (optional)
# df = df[(df["year"] >= 2016) & (df["year"] <= 2024)]  # ignore 2008–2015 if needed

# Count number of posts per year
post_countsr = querytrendr["year"].value_counts().sort_index()
post_countsy = querytrendy["year"].value_counts().sort_index()
# Plot
plt.figure(figsize=(10, 5))
plt.plot(post_countsr.index, post_countsr.values, marker='o', linestyle='-', color='orange', label='Reddit')
plt.plot(post_countsy.index, post_countsy.values, marker='o', linestyle='-', color='red', label='YouTube')
plt.title("Total Number of Posts per Year(Health & Mental Well-being)")
plt.xlabel("Year")
plt.ylabel("Number of Posts")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
