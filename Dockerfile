# Use the official Python image from the Docker Hub
FROM python:3.13-slim

# Create a non-root user
RUN useradd -m fastapiuser

# Update the image
RUN apt update && apt upgrade -y

# Globally install uv
RUN pip install uv

# Set the working directory
WORKDIR /app

# Copy the code into the image
COPY pyproject.toml uv.lock ./
COPY qherde ./qherde/

# Change the ownership of the application files to the non-root user
# This has to be done before `uv sync`, otherwise Python (symlinked in .venv) will be owned by the chown-ed user
RUN chown -R fastapiuser:fastapiuser /app

# Install the dependencies
RUN uv sync

# Switch to the non-root user
USER fastapiuser

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["uv", "run", "uvicorn", "qherde.main:app", "--host", "0.0.0.0", "--port", "8000"]