from pymongo import MongoClient
from config import MONGO_URI, DB_NAME

client = MongoClient(MONGO_URI)

db = client[DB_NAME]

invoice_collection = db["invoices"]

print("MongoDB Connected Successfully")