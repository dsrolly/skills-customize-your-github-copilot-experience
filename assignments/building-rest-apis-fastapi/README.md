📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API for a library catalog using FastAPI. You will practice defining routes, validating request data, and returning JSON responses.

## 📝 Tasks

### 🛠️ Create a Book API

#### Description
Use the starter code to create a FastAPI application with an in-memory list of books. Run the app locally and explore it in the interactive API documentation.

#### Requirements
Completed program should:

- Use FastAPI to define a `GET /` route that returns a welcome message
- Use Pydantic to define a `Book` model with `title`, `author`, and `year` fields
- Store books in a list in memory
- Run with `uvicorn main:app --reload`

### 🛠️ Add CRUD Endpoints

#### Description
Extend the application so students can add, view, and update books.

#### Requirements
Completed program should:

- Add `POST /books` to accept a book and append it to the catalog
- Add `GET /books` to return all books
- Add `GET /books/{book_id}` to return one book by its position in the list
- Return a 404 response when a requested book ID does not exist

### 🛠️ Validate and Delete Books

#### Description
Improve the API with validated updates and a deletion endpoint.

#### Requirements
Completed program should:

- Validate that `year` is greater than 0
- Add `PUT /books/{book_id}` to replace an existing book
- Add `DELETE /books/{book_id}` to remove a book
- Return clear JSON responses for successful updates and deletions
- Stretch goal: Add a search route that filters books by author
