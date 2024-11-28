FROM python:3.13-slim

# Set the working directory
WORKDIR /app

# Install system dependencies for building cx-Oracle and other packages
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    gcc \
    libaio1 \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy Oracle Instant Client
COPY instantclient /usr/lib/oracle/instantclient

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Set the command to run the application (if applicable)
CMD ["python", "your_script.py"]
