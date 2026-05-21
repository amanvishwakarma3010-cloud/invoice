from pymongo import MongoClient

MONGO_URI = "mongodb+srv://library_user:Library123@cluster0.cxhkego.mongodb.net/library_management?retryWrites=true&w=majority"

try:
    client = MongoClient(MONGO_URI)

    db = client["library_management"]

    db.command("ping")

    print("MongoDB Atlas Connected Successfully")

except Exception as e:
    print("Connection Error:")
    print(e)