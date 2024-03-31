# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies
RUN apt-get update && \
    apt-get install -y libzbar-dev && \
    pip install --no-cache-dir opencv-python-headless pyzbar

# Run the Python script when the container launches
CMD ["python", "qr_code_reader.py"]
