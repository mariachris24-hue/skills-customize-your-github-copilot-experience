from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from typing import List

app = FastAPI()
DATABASE = "books.db"

class Book(BaseModel):
    id: int
    title: str
    author: str
    published_year: int

class BookCreate(BaseModel):
    title: str
    author: str
    published_year: int

class BookUpdate(BaseModel):
    title: str
    author: str
    published_year: int

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            published_year INTEGER NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()

@app.on_event("startup")
def startup_event():
    init_db()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI SQLite Books API!"}

@app.get("/books", response_model=List[Book])
def list_books():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM books").fetchall()
    conn.close()
    return [Book(**dict(row)) for row in rows]

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    conn = get_connection()
    row = conn.execute("SELECT * FROM books WHERE id = ?", (book_id,)).fetchone()
    conn.close()
    if row is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return Book(**dict(row))

@app.post("/books", response_model=Book, status_code=201)
def create_book(book: BookCreate):
    conn = get_connection()
    cursor = conn.execute(
        "INSERT INTO books (title, author, published_year) VALUES (?, ?, ?)",
        (book.title, book.author, book.published_year),
    )
    conn.commit()
    book_id = cursor.lastrowid
    conn.close()
    return Book(id=book_id, **book.dict())

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book: BookUpdate):
    conn = get_connection()
    cursor = conn.execute("SELECT * FROM books WHERE id = ?", (book_id,))
    row = cursor.fetchone()
    if row is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Book not found")
    conn.execute(
        "UPDATE books SET title = ?, author = ?, published_year = ? WHERE id = ?",
        (book.title, book.author, book.published_year, book_id),
    )
    conn.commit()
    conn.close()
    return Book(id=book_id, **book.dict())

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    conn = get_connection()
    cursor = conn.execute("SELECT * FROM books WHERE id = ?", (book_id,))
    row = cursor.fetchone()
    if row is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Book not found")
    conn.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()
    conn.close()
    return {"detail": "Book deleted successfully"}
