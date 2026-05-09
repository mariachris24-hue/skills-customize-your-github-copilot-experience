# 📘 Assignment: Building Database-Backed APIs with FastAPI and SQLite

## 🎯 Objective

Extend your FastAPI skills by building a REST API that stores data in SQLite. Students will learn how to model data, persist records, and perform CRUD operations with a simple database backend.

## 📝 Tasks

### 🛠️ Task 1: Set up FastAPI with SQLite

#### Description
Create a FastAPI project with a SQLite database connection.

#### Requirements
Completed project should:

- Install `fastapi`, `uvicorn`, and `sqlite3` (standard library)
- Create the app in `main.py`
- Connect to a SQLite database file named `books.db`
- Add a `GET /` endpoint that returns a welcome message

### 🛠️ Task 2: Define database models and Pydantic schemas

#### Description
Model the data for a simple book resource and use Pydantic for request validation.

#### Requirements
Completed project should:

- Create a `Book` schema with `id`, `title`, `author`, and `published_year`
- Use Pydantic models for request and response validation
- Store books in a SQLite table named `books`

### 🛠️ Task 3: Implement CRUD endpoints

#### Description
Build routes to create, read, update, and delete books.

#### Requirements
Completed project should:

- Add `GET /books` to return all books
- Add `GET /books/{book_id}` to return a single book by ID
- Add `POST /books` to create a new book
- Add `PUT /books/{book_id}` to update a book
- Add `DELETE /books/{book_id}` to remove a book

### 🛠️ Task 4: Handle validation and errors

#### Description
Ensure the API returns clear errors for bad input and missing records.

#### Requirements
Completed project should:

- Return `400` for invalid requests or duplicate book IDs
- Return `404` when the requested book is not found
- Return JSON error messages

### 🛠️ Task 5: Verify the API

#### Description
Use FastAPI docs or HTTP requests to test the API behavior.

#### Requirements
Completed project should:

- Confirm `GET /docs` is available
- Verify `POST /books` creates a new book
- Verify `GET /books`, `GET /books/{book_id}`, `PUT /books/{book_id}`, and `DELETE /books/{book_id}` work as expected
