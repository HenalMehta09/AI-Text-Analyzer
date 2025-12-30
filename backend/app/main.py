from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import requests

app = FastAPI()

# ✅ CORS (THIS IS THE FIX)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # OK for learning/dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

AI_SERVICE_URL = os.getenv("AI_SERVICE_URL", "http://localhost:8001")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/predict")
def predict(text: str):
    try:
        response = requests.get(
            f"{AI_SERVICE_URL}/analyze",
            params={"text": text},
            timeout=3
        )
        response.raise_for_status()
    except requests.RequestException as e:
        return {
            "error": "AI service unavailable",
            "details": str(e)
        }

    return {
        "input": text,
        "ai_result": response.json()
    }
