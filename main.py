import os
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
from io import BytesIO
import secureocr  # Using the imported library

# Set Tesseract data path (Modify as needed)
os.environ["TESSDATA_PREFIX"] = "/usr/share/tesseract-ocr/5/tessdata"

# Initialize FastAPI app
app = FastAPI()

# Enable CORS for any origin, method, and header
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow any origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

@app.post("/ocr/")
async def ocr_image(file: UploadFile = File(...)):
    """Receives an image file, extracts text using OCR, and returns the text."""
    try:
        # Read image into PIL format
        image = Image.open(BytesIO(await file.read()))

        # Perform OCR using the secureocr library
        extracted_text = secureocr.extract_text(image)

        return {"filename": file.filename, "text": extracted_text}
    except Exception as e:
        return {"error": str(e)}

# Root route for health check
@app.get("/")
def home():
    return {"message": "OCR Service is running!"}
