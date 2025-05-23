FROM python:3.13-alpine

WORKDIR /app

COPY . /app

RUN pip install fastapi uvicorn docker

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
