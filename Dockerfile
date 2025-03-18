FROM python:3.9

RUN pip install pandas sqlalchemy psycopg2

WORKDIR /app

COPY . .

ENTRYPOINT ["python", "main.py"]