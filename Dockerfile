# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy all files from the project directory to the container
COPY . /app

# Install dependencies
RUN pip install flask

# Define the command to run the API
CMD ["python", "app.py"]
