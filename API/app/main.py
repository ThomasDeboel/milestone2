
from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException

app = FastAPI()

origins = [
    "http://localhost:8000",  # Allow localhost for development
    "http://localhost",  # Allow localhost without port
    "http://localhost:8080",  # Allow localhost with port 8080
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    name: str


client = MongoClient("mongodb://:27017/")
db = client["mydatabase"]
collection = db["users"]

@app.get("/user")
async def get_user(user_name: str):
    user = await collection.find_one({"name": user_name})
    return user["name"]

@app.post("/user")
async def create_user(user: User):
    user_data = {"name": "frietje jansens"}
    collection.insert_one(user_data)
    return user

@app.put("/user/{user_name}")
async def update_user(user_name: str, user: User):
    existing_user = collection.find_one({"name": user_name})
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    collection.update_one({"name": user_name}, {"$set": user.model_dump()})
    return {"message": "User updated successfully"}