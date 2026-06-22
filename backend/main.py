from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {
        "message" : "Welcome to MODELFORAGE"
    }

@app.get("/health")
def health_check():
    return {
        "status" : "healthy",
        "service" : "ModelForage Backend"
    }