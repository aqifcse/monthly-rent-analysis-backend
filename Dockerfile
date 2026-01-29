# Use the official lightweight Python image.
# You can change the version as needed.
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app
# Copy your application code to the container.
# This assumes your FastAPI code (e.g., main.py, requirements.txt etc) is in the current directory.
COPY . .
# Install the Python dependencies.
# The '--no-cache-dir' flag reduces the image size by not caching the installation packages.
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
# Install netcat-openbsd for waiting on Postgres.
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*
# Expose port 80 to allow external access to the FastAPI application.
EXPOSE 8000
# Define the command to run the application using Uvicorn.
# Here, 'main:app' means that the FastAPI app is instantiated in a file named 'main.py'
# with the variable 'app' (e.g., app = FastAPI()).
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
