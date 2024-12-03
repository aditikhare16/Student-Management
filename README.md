# Student Management System API

This project is a **Student Management System API** built using **FastAPI** and **MongoDB**. It provides a backend solution for managing students' information, including creating, retrieving, updating, and deleting student records. The database is hosted on MongoDB Atlas.

---

## Features

- **Add a new student**
- **Retrieve a student's details**
- **Update a student's details**
- **Delete a student's record**
- **List all students**

---

## Tech Stack

- **Backend Framework**: FastAPI
- **Database**: MongoDB (Atlas M0 Free Cluster)
- **ORM/Driver**: Motor
- **Programming Language**: Python

---

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.8 or higher
- Pip (Python package manager)
- A MongoDB Atlas account (for database hosting)

---

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/student-management-system.git
   cd student-management-system
   ```

2. **Create a Virtual Environment** (Optional but recommended)

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate    # On Windows
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up MongoDB Atlas**

   - Create a MongoDB Atlas cluster and get the connection string.
   - Replace `<username>`, `<password>`, and `<cluster-url>` with your MongoDB credentials in the `database.py` file:

     ```python
     MONGO_URI = "mongodb+srv://<username>:<password>@<cluster-url>/?retryWrites=true&w=majority"
     ```

5. **Run the Application**

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```

6. **Access the Application**

   - Open your browser and navigate to: `http://127.0.0.1:8000`
   - Use Swagger UI for testing the APIs: `http://127.0.0.1:8000/docs`

---

## API Endpoints

### **Base URL**: `http://127.0.0.1:8000`

| Method | Endpoint           | Description                 |
|--------|--------------------|-----------------------------|
| GET    | `/students/{id}`   | Get details of a student    |
| POST   | `/students`        | Add a new student           |
| PUT    | `/students/{id}`   | Update student information  |
| DELETE | `/students/{id}`   | Delete a student            |
| GET    | `/students`        | List all students           |

---

## Folder Structure

```
student-management-system/
├── main.py       # Entry point of the application
├── models.py     # Pydantic models for request validation
├── database.py   # MongoDB connection setup
├── routes.py     # API route definitions
├── utils.py      # Utility functions
├── requirements.txt # Project dependencies
└── README.md     # Project documentation
```





