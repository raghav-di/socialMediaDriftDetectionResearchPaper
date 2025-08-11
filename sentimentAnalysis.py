import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

analyzer = SentimentIntensityAnalyzer()

df["sentiment_score"] = df["clean_text"].apply(lambda x: analyzer.polarity_scores(x))
k = 8
df["sentiment_label"] = df["sentiment_score"].apply(
    lambda x: "positive" if (x['pos'] > x['neu']**k and x['pos'] > x['neg']) else ("negative" if (x['neg'] > x['neu']**k and x['neg'] > x['pos']) else "neutral")
)
df["sentiment_compound"] = df["sentiment_score"].apply(lambda x: x['compound'])
df["positive_score"] = df["sentiment_score"].apply(lambda x: x['pos'])
df["neutral_score"] = df["sentiment_score"].apply(lambda x: x['neu'])
df["negative_score"] = df["sentiment_score"].apply(lambda x: x['neg'])
