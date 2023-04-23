FROM python:3.9
WORKDIR /docker
ADD . /docker
RUN pip install --no-cache-dir --upgrade -r requirements.txt
CMD [ "python" , "/docker/app.py" ]
RUN chown -R 42420:42420 /docker
ENV HOME=/docker

