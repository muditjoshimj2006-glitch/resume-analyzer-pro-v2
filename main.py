#Resume analyzer pro
from fastapi import FastAPI
from app.routers.resume import router

app = FastAPI()
app.include_router(router)

#Routers
@app.get("/")
def home():
    return {
        "message" : "Welcome to the resume analyzer pro v2"
    }

