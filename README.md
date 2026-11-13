# Product Inventory Management System

A full-stack product inventory management application built with **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and a **React** frontend. It provides a complete CRUD (Create, Read, Update, Delete) interface to manage product catalogs, inventory levels, and pricing.

---

## Features

- **Full CRUD REST API**: Create, view, update, and delete products seamlessly.
- **Data Validation & Typing**: Strong validation using Pydantic schemas.
- **Relational Persistence**: PostgreSQL database integration via SQLAlchemy ORM.
- **Interactive API Documentation**: Auto-generated interactive Swagger UI and ReDoc.
- **Database Auto-Seeding**: Seeds initial product catalog if the database table is empty.
- **React Frontend**: Clean, responsive UI with live search/filter, sorting, and modal forms for adding and editing products.
- **CORS Configured**: Pre-configured cross-origin sharing for local frontend and backend communication.

---

## Tech Stack

### Backend
- **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **ASGI Server**: [Uvicorn](https://www.uvicorn.org/)
- **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/)
- **Validation**: [Pydantic](https://docs.pydantic.dev/)
- **Database Driver**: [psycopg2](https://www.psycopg.org/)
- **Database**: PostgreSQL
- **Package Manager**: [uv](https://github.com/astral-sh/uv) / pip

### Frontend
- **Library**: [React 18](https://react.dev/)
- **HTTP Client**: [Axios](https://axios-http.com/)
- **Styling**: Modern Vanilla CSS

---

## Project Structure

```text
FastApi_project/
├── database.py         # SQLAlchemy engine and session setup
├── database_model.py   # SQLAlchemy ORM model (Product entity / datasheet table)
├── models.py           # Pydantic validation schema (Product)
├── main.py             # FastAPI entrypoint, routes, middleware, and seed logic
├── pyproject.toml      # Python dependencies and project metadata
├── uv.lock             # uv dependency lockfile
├── frontend/           # React frontend application
│   ├── package.json    # Frontend dependencies and scripts
│   ├── public/         # Static HTML template and assets
│   └── src/            # React components (App.js, TaglineSection.js, styles)
└── README.md           # Project documentation
```

---

## Getting Started

### Prerequisites

Ensure you have the following installed on your machine:
- **Python 3.13+** (or compatible 3.10+)
- **PostgreSQL** server running locally
- **Node.js** (v16+) and **npm**
- **uv** (recommended) or standard `pip`

---

### 1. Database Setup

1. Start your local PostgreSQL service.
2. Create a database named `product`:
   ```sql
   CREATE DATABASE product;
   ```
3. Update connection credentials in `database.py` if your PostgreSQL username or password differs from the default:
   ```python
   # database.py
   db_url = "postgresql://<username>:<password>@localhost:5432/product"
   ```

---

### 2. Backend Setup

1. Open a terminal in the project root:
   ```bash
   cd FastApi_project
   ```

2. Install dependencies:
   * **Using `uv` (recommended)**:
     ```bash
     uv sync
     ```
   * **Using `pip`**:
     ```bash
     python -m venv .venv
     source .venv/bin/activate  # On Windows: .venv\Scripts\activate
     pip install fastapi uvicorn sqlalchemy psycopg2 pydantic
     ```

3. Run the development server:
   * **Using `uv`**:
     ```bash
     uv run uvicorn main:app --reload
     ```
   * **Using active virtual environment**:
     ```bash
     uvicorn main:app --reload
     ```

The backend server will start at **`http://localhost:8000`**.

Interactive API docs will be accessible at:
- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

### 3. Frontend Setup

1. In a new terminal window, navigate to the `frontend` folder:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   ```

The application will automatically open at **`http://localhost:3000`**.

---

## API Reference

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Health check / greeting endpoint |
| `GET` | `/products` | Retrieve list of all products |
| `GET` | `/products/{id}` | Retrieve a single product by ID |
| `POST` | `/products` | Create and save a new product |
| `PUT` | `/products/{id}` | Update product details by ID |
| `DELETE` | `/products/{id}` | Delete a product by ID |

### Product Data Schema

```json
{
  "id": 1,
  "name": "Smartphone",
  "description": "5G Android Smartphone",
  "price": 699.99,
  "quantity": 25
}
```

---

## License

This project is open-source and available under the [MIT License](LICENSE).

# Product-Management-System
