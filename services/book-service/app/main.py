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

fake_books = [
    {"id": 1, "title": "One Flew Over the Cuckoo's Nest", "isbn": "978-0451163967"},
    {"id": 2, "title": "The Redbreast", "isbn": "978-0061133992"},
    {"id": 3, "title": "The Bat", "isbn": "978-1846551451"},
    {"id": 4, "title": "Hunger (Penguin Twentieth Century Classics)", "isbn": "978-0141180649"}
]

class Book(BaseModel):
    id: int
    title: str
    isbn: str

@app.get('/', response_model=List[Book])
async def get_books():
    return fake_books

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3001)