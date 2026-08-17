# Use a minimal Base image with python 3.9 installed
FROM python: 3.9 -slim

# Set the working directory inside the container to/app
WORKDIR /app

# Copy all files from the current directory on the host to the container's /app directory
COPY . .

# Install python dependencies listed in requirements.txt
RUN pip3 instal -r requirements.txt

# Define the command to run the Streamlit app on port 8501 and make it accessible externally
CMD ["Streamlit", "run", "app.py", "--server.port", "8501", "--server.enableCORS", "false", "--server.enableXsrfProtection", "false"]
