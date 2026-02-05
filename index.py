from fastapi import FastAPI
import requests
import random

app = FastAPI()

NAMES_MS_URL = "http://names-ms-v1:8000/api/v1/names"



@app.get("/")
def root():
    return {"message": "Welcome to KITTENS ms!"}

@app.get("/api/v1/kittens")
def get_kittens():
    kittens = [
        "Black kitty",
        "White kitty",
        "Whiskers",
        "Shadow",
        "Miu miu kitty"
    ]

    # Call names microservice
    response = requests.get(NAMES_MS_URL)
    names_dict = response.json()
    names = list(names_dict.values())

    # Assign random name to each kitten
    result = []
    for kitten in kittens:
        result.append({
            "kitten": kitten,
            "name": random.choice(names)
        })

    return result
