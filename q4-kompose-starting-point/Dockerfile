# imagem base
FROM python:3.9


COPY . /code/

WORKDIR /code

RUN apt update \
    && apt install -y libpq-dev gcc 

RUN pip install -r requirements.txt
RUN pip install psycopg2

ENV PYTHONDONTWRITEBYTECODE 1



