# 📘 Assignment: Persistent Library API

## 🎯 Objective

Extend a FastAPI library catalog with a SQLite database so books remain available after the application restarts.

## 📝 Tasks

### 🛠️ Create the Database Schema

#### Description
Use SQLite to create a persistent table for the library catalog and establish a connection pattern for database operations.

#### Requirements
Completed program should:

- Import Python's built-in `sqlite3` module
- Create a database file named `library.db`
- Create a `books` table with `id`, `title`, `author`, and `year` columns
- Set `id` as an integer primary key
- Initialize the table when the application starts

### 🛠️ Add and List Books

#### Description
Replace the in-memory book collection with database-backed create and read operations.

#### Requirements
Completed program should:

- Use parameterized SQL statements to insert a book
- Return the new book, including its database-generated ID
- Return all books from the database as a list
- Read database values into dictionaries or Pydantic models

### 🛠️ Retrieve and Modify Books

#### Description
Use database IDs to retrieve, update, and delete individual catalog entries.

#### Requirements
Completed program should:

- Add `GET /books/{book_id}` to return one book or a 404 response
- Add `PUT /books/{book_id}` to update an existing book
- Add `DELETE /books/{book_id}` to remove an existing book
- Raise 404 with `"Book not found"` when an ID does not exist
- Validate that `year` is greater than 0

### 🛠️ Search the Catalog

#### Description
Add a database query that helps users find books by author.

#### Requirements
Completed program should:

- Add `GET /books/search/` accepting an `author` query parameter
- Match authors using SQL `LIKE` with parameterized values
- Return a list of matching books
- Protect the SQL query from injection by keeping user input as a parameter

#### Stretch Goal

- Add ordering for search results by title or year
- Add an endpoint that counts all books in the database
- Test that data remains after restarting Uvicorn
