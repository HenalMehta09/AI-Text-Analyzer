from fastapi import FastAPI
from typing import List
import re

app = FastAPI()

POSITIVE_WORDS = {
    "love", "great", "awesome", "happy", "good", "excellent", "amazing"
}

NEGATIVE_WORDS = {
    "hate", "bad", "sad", "terrible", "awful", "poor", "worst"
}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/analyze")
def analyze(text: str):
    words = re.findall(r"\b\w+\b", text.lower())

    pos_count = sum(word in POSITIVE_WORDS for word in words)
    neg_count = sum(word in NEGATIVE_WORDS for word in words)

    if pos_count > neg_count:
        sentiment = "positive"
    elif neg_count > pos_count:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    keywords: List[str] = list(set(words))

    return {
        "sentiment": sentiment,
        "keywords": keywords,
        "positive_score": pos_count,
        "negative_score": neg_count
    }
