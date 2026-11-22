from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Library Catalog API")


class Book(BaseModel):
    title: str
    author: str
    year: int = Field(gt=0)


books: list[Book] = []


@app.get("/")
def welcome():
    return {"message": "Welcome to the Library Catalog API"}


@app.get("/books")
def get_books():
    # TODO: Return the list of books.
    return []


@app.post("/books")
def add_book(book: Book):
    # TODO: Add the book to the in-memory list and return it.
    return book


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Return the requested book or raise HTTPException(status_code=404).
    raise HTTPException(status_code=404, detail="Book not found")
