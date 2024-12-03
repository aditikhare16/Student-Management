from bson import ObjectId

def serialize_student(student):
    """
    Converts a MongoDB student document to a serialized response format.
    Args:
        student (dict): The MongoDB document for a student.
    Returns:
        dict: A serialized dictionary with id instead of _id.
    """
    return {
        "id": str(student["_id"]),  # Convert ObjectId to string
        "name": student["name"],
        "age": student["age"],
        "gender": student["gender"],
        "address": student.get("address"),  # Optional field
    }
