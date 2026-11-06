from fastapi import FastAPI

app = FastAPI()

# Home Route
app.get("/")
def home():
    return {"message": "home"}