# Base image with Python and Streamlit
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose the port Streamlit runs on
EXPOSE 8501


# Command to run the Streamlit app
CMD ["streamlit", "run", "Homepage.py"]
