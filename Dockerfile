FROM python:3.7-alpine

WORKDIR /usr/src

RUN apk --no-cache add mariadb-dev build-base

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache

COPY . .

CMD ["python", "-m", "library"]