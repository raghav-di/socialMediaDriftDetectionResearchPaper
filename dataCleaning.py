import re

df["full_text"] = df["title"].fillna('') + " " + df["text"].fillna('')

def clean_text(text):
    text = re.sub(r"http\S+", "", text)  # remove URLs
    text = re.sub(r"[^\w\s]", "", text)  # remove punctuation
    text = re.sub(r"\d+", "", text)      # remove numbers
    text = text.lower().strip()
    return text

df["clean_text"] = df["full_text"].apply(clean_text)
