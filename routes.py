from fastapi import APIRouter, HTTPException, status
from database import db
from models import Student, UpdateStudent
from bson import ObjectId
from typing import List

# Router setup
student_router = APIRouter(prefix="/students", tags=["Students"])

# Helper function to convert BSON to JSON
def student_helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "name": student["name"],
        "age": student["age"],
        "gender": student["gender"],
        "percentage": student["percentage"],
        "image_url": student.get("image_url"),
    }

# Create a new student
@student_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_student(student: Student):
    student_dict = student.dict()
    result = await db.students.insert_one(student_dict)
    created_student = await db.students.find_one({"_id": result.inserted_id})
    return student_helper(created_student)

# Get all students
@student_router.get("/", response_model=List[dict])
async def get_all_students():
    students = await db.students.find().to_list(100)
    return [student_helper(student) for student in students]

# Get a single student by ID
@student_router.get("/{student_id}", response_model=dict)
async def get_student(student_id: str):
    student = await db.students.find_one({"_id": ObjectId(student_id)})
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Student not found"
        )
    return student_helper(student)

# Update a student
@student_router.put("/{student_id}", response_model=dict)
async def update_student(student_id: str, student: UpdateStudent):
    update_data = {k: v for k, v in student.dict().items() if v is not None}
    if update_data:
        result = await db.students.update_one(
            {"_id": ObjectId(student_id)}, {"$set": update_data}
        )
        if result.modified_count == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Student not found"
            )
    updated_student = await db.students.find_one({"_id": ObjectId(student_id)})
    return student_helper(updated_student)

# Delete a student
@student_router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_student(student_id: str):
    result = await db.students.delete_one({"_id": ObjectId(student_id)})
    if result.deleted_count == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Student not found"
        )
    return {"message": "Student deleted successfully"}
