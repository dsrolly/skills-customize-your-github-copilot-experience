import sqlite3

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

DATABASE = "library.db"

app = FastAPI(title="Persistent Library API")


class Book(BaseModel):
    title: str
    author: str
    year: int = Field(gt=0)


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year INTEGER NOT NULL
            )
            """
        )


initialize_database()


@app.get("/")
def welcome():
    return {"message": "Welcome to the Persistent Library API"}


@app.get("/books")
def get_books():
    # TODO: Select and return all books ordered by id.
    return []


@app.post("/books")
def add_book(book: Book):
    # TODO: Insert book into SQLite and return it with its database id.
    return {"id": None, **book.model_dump()}


@app.get("/books/search/")
def search_books(author: str):
    # Stretch: Select books whose author matches with SQL LIKE.
    return []


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Select one book by id or raise HTTPException(status_code=404).
    raise HTTPException(status_code=404, detail="Book not found")


@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    # TODO: Update the matching book and return the saved result.
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    # TODO: Delete the matching book or raise HTTPException(status_code=404).
    raise HTTPException(status_code=404, detail="Book not found")
