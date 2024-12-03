from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://atlas-sql-674ea77c614e9802ad132fc7-ceevj.a.query.mongodb.net/myVirtualDatabase?ssl=true&authSource=admin"

async def test_connection():
    client = AsyncIOMotorClient(MONGO_URI)
    db = client.test
    print(await db.command("ping"))

import asyncio
asyncio.run(test_connection())
