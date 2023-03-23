import logging
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

fake_users = [
    {"id": 1, "name": "Mickey Mouse", "username": "metalmickey"},
    {"id": 2, "name": "Ellen Ripley", "username": "acidblood"}
]

class User(BaseModel):
    id: int
    name: str
    username: str

@app.get('/', response_model=List[User])
async def get_users():
    return fake_users

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)