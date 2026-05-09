# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a REST API using FastAPI. Students will define routes, request/response models, and handle validation and errors.

## 📝 Tasks

### 🛠️ Task 1: Set up the FastAPI project

#### Description
Create a FastAPI application and add a root endpoint.

#### Requirements
Completed project should:

- Install `fastapi` and `uvicorn`
- Create a FastAPI app in `main.py`
- Add a `GET /` endpoint that returns a welcome message
- Run the app locally with `uvicorn main:app --reload`

### 🛠️ Task 2: Create data models and routes

#### Description
Define a Pydantic model and build endpoints for a book resource.

#### Requirements
Completed project should:

- Define a `Book` model with fields: `id`, `title`, `author`, `published_year`
- Add a `GET /books` endpoint that returns a list of books
- Add a `GET /books/{book_id}` endpoint that returns a single book by ID
- Add a `POST /books` endpoint that creates a new book

### 🛠️ Task 3: Add validation and error handling

#### Description
Ensure incoming requests are validated and errors are returned clearly.

#### Requirements
Completed project should:

- Use Pydantic validation for incoming `POST` data
- Return `400` for invalid payloads
- Return `404` when a requested book ID is not found
- Include informative JSON error responses

### 🛠️ Task 4: Test the API endpoints

#### Description
Verify the API using FastAPI docs or HTTP requests.

#### Requirements
Completed project should:

- Confirm `GET /docs` is available
- Check that `POST /books` creates a new book
- Verify `GET /books` and `GET /books/{book_id}` return the correct data
