FROM python:3.9

WORKDIR /docker

ADD . /docker

RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Set up a new user named "user" with user ID 1000
RUN useradd -m -u 1000 user

# Switch to the "user" user
USER user

# Set home to the user's home directory
ENV HOME=/home/user \
	PATH=/home/user/.local/bin:$PATH

# Set the working directory to the user's home directory
WORKDIR $HOME/app

# Set the working directory to the user's home directory
COPY --chown=user . $HOME/app

CMD [ "gunicorn" , "/docker/app.py" ]