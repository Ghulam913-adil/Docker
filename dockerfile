# Base image
FROM python:3.13-slim

# Working directory
WORKDIR /app

# Copy files
COPY requirements.txt ./
COPY scripts ./scripts
COPY data ./data

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command
CMD ["python", "scripts/train_model.py"]
