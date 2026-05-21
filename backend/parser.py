import google.generativeai as genai
from PIL import Image
from config import GEMINI_API_KEY
import json

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def extract_invoice_from_image(image_path):

    image = Image.open(image_path)

    prompt = """
You are an invoice extraction expert.

Extract invoice data from this invoice image.

Return ONLY valid JSON.

{
  "invoice_number": "",
  "vendor_name": "",
  "invoice_date": "",
  "gst_number": "",
  "subtotal": null,
  "tax_amount": null,
  "total_amount": null,
  "currency": "INR",
  "items": [
    {
      "description": "",
      "quantity": null,
      "unit_price": null,
      "amount": null
    }
  ]
}

Rules:
- Do not guess.
- Extract values exactly as shown.
- Return only JSON.
- Preserve GST number exactly.
- Preserve invoice number exactly.
"""

    response = model.generate_content(
        [prompt, image]
    )

    cleaned = (
        response.text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    return json.loads(cleaned)