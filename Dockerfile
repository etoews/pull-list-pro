FROM python:3.6-alpine

RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev

WORKDIR /pull-list-pro

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["flask", "run"]
