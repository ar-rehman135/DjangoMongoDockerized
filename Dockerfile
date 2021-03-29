FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /code


WORKDIR /code

COPY . /code/

RUN apt-get install gcc

RUN pip install -r requirements.txt

ADD . /code