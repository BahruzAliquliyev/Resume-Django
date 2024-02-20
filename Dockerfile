# Pull official base image
FROM python:3.10-slim


RUN apt update && apt install -y python3-dev build-essential python3


# pip requirements

RUN pip install --upgrade pip
RUN pip install virtualenv && python -m virtualenv /opt/venv

ADD ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY . /srv/
WORKDIR /srv/sudo app


