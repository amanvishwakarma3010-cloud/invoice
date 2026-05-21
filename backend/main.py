from fastapi import FastAPI
from fastapi import UploadFile
from fastapi import File

from db import invoice_collection
from parser import extract_invoice_from_image

import shutil
import os
from datetime import datetime

app = FastAPI()

# FIXED PATH SECTION

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

UPLOAD_DIR = os.path.join(
    BASE_DIR,
    "uploads"
)

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)

# END FIX


@app.get("/")
def home():

    return {
        "message": "Invoice AI Running"
    }


@app.post("/upload")
async def upload_invoice(
    file: UploadFile = File(...)
):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    invoice_data = extract_invoice_from_image(
        file_path
    )

    invoice_data["file_name"] = (
        file.filename
    )

    invoice_data["created_at"] = (
        datetime.utcnow().isoformat()
    )

    result = invoice_collection.insert_one(
        invoice_data
    )

    invoice_data["_id"] = str(
        result.inserted_id
    )

    return invoice_data


@app.get("/invoices")
def get_all_invoices():

    invoices = []

    for invoice in invoice_collection.find():

        invoice["_id"] = str(
            invoice["_id"]
        )

        invoices.append(invoice)

    return invoices


@app.get("/invoice/{invoice_number}")
def get_invoice(invoice_number):

    invoice = invoice_collection.find_one(
        {
            "invoice_number":
            invoice_number
        }
    )

    if invoice:

        invoice["_id"] = str(
            invoice["_id"]
        )

    return invoice