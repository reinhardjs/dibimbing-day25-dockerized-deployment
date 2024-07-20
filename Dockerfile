FROM python:3.8-slim as python-base
ENV ENV=production \
    POETRY_VERSION=1.1.12 \
    PORT=8001
RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential
WORKDIR /app
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt
WORKDIR /app
COPY . /app
EXPOSE 8001
ENTRYPOINT /usr/local/bin/uvicorn main:app --host 0.0.0.0 --port $PORT
