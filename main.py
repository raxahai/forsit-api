from fastapi import FastAPI

app = FastAPI(title="Forsit backend",
              description="This is a test by Forsit", version="0.0.1")


@app.get('/', status_code=200)
def home():
    return "This is home page"
