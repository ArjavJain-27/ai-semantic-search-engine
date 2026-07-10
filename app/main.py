from fastapi import FastAPI

app = FastAPI(
    title="AI Semantic Search Engine",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to AI Semantic Search Engine 🚀"
    }