from pydantic import BaseModel, Field
from typing import Optional

# Student Model
class Student(BaseModel):
    name: str
    age: int
    gender: str
    percentage: float
    image_url: Optional[str] = None

# Update Student Model
class UpdateStudent(BaseModel):
    name: Optional[str]
    age: Optional[int]
    gender: Optional[str]
    percentage: Optional[float]
    image_url: Optional[str]
