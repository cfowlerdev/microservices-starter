import logging
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

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