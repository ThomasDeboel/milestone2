from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    name: str


client = MongoClient("mongodb://root:example@mongo-td:27017/")
db = client["mydatabase"]
collection = db["users"]

@app.get("/user")
async def get_user():
    user = collection.find_one()
    return {"username": user["name"]}

@app.post("/user")
async def create_user(user: User):
    user_data = {"name": "Thomas Deboel"}
    collection.insert_one(user_data)
    return user

@app.post("/changeuser")
async def update_user():
    collection.update_one({"name": "Thomas Deboel"}, {"$set": {"name": "Frietje Jansens"}})
    return {"message": "User updated"}