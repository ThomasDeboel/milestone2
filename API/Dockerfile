# Use the Python 3.10.0 base image
FROM python:3.10.0

# Set the working directory to /code
WORKDIR /code

# Expose port 8000 for the application
EXPOSE 8000

# Copy the requirements.txt file to the /code directory
COPY ./requirements.txt /code/requirements.txt

# Install the required Python packages from requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the app directory to the /code directory
COPY ./app /code/app

# Set the command to run the application using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]