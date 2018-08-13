# Use Python 3.6 as the base image
FROM python:3.6

# Change directory inside the container
WORKDIR /usr/src/app

# Copy all the files from the current directory of the host to the current directory of the container
COPY ./ ./

# Install the project in editable mode
RUN pip install -e .

# Install the packages from the requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Export the environment variables for development
ENV FLASK_APP=app
ENV FLASK_DEBUG=true

# Finally, run the app using the Flask CLI (0.0.0.0 should be used so that it will be visible outside of the container)
CMD flask run --host=0.0.0.0
