FROM python:3.7

RUN apt-get update && apt-get install netcat -y

COPY ./src /app
WORKDIR /app

CMD ["python", "/app/main.py"]