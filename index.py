from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return  {"message" : "Welcome to KITTENS ms!"} 

@app.get("/api/v1/kittens")
def get_kittens():
    return {
        "1": "Black kitty",
        "2": "White kitty",
        "3": "Whiskers",
        "4": "Shadow",
        "5": "Miu miu kitty"
    }