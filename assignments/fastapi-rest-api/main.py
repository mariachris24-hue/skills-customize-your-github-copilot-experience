from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    published_year: int

books: List[Book] = [
    Book(id=1, title="Learning FastAPI", author="A. Teacher", published_year=2025),
    Book(id=2, title="Python APIs", author="B. Student", published_year=2024),
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI book API!"}

@app.get("/books", response_model=List[Book])
def list_books():
    return books

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books", response_model=Book, status_code=201)
def create_book(book: Book):
    if any(existing.id == book.id for existing in books):
        raise HTTPException(status_code=400, detail="Book with this ID already exists")
    books.append(book)
    return book
