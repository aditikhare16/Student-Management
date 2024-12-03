from motor.motor_asyncio import AsyncIOMotorClient
from decouple import config


# MongoDB connection
MONGO_URI = config("MONGO_URI")  # Added this in .env file 
client = AsyncIOMotorClient(MONGO_URI)
db = client["student_management"]
students_collection = db["students"]
