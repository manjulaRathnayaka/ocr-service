FROM python:3.9-slim

# Install Tesseract OCR
RUN apt-get update && apt-get install -y tesseract-ocr libtesseract-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user with UID 10001 (Choreo requirement)
RUN groupadd -g 10001 choreo && \
    useradd -u 10001 -g choreo -s /bin/bash -m choreo

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy service code
COPY . .

# Set proper permissions
RUN chown -R choreo:choreo /app

# Switch to non-root user
USER 10001

# Expose port
EXPOSE 8000

# Start FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
