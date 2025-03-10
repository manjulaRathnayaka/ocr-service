# OCR Service

A FastAPI service that extracts text from images using `secureocr`.

## Installation

1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

2. Run the service:
   ```sh
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

## Usage

Send a POST request with an image:

```sh
curl -X 'POST'   'http://127.0.0.1:8000/ocr/'   -H 'accept: application/json'   -H 'Content-Type: multipart/form-data'   -F 'file=@sample.png'
```

Response:

```json
{
    "filename": "sample.png",
    "text": "Detected text from image"
}
```

## Docker

To run in Docker:

```sh
docker build -t ocr-service .
docker run -p 8000:8000 ocr-service
```
