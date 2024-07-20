FROM python:3.8-slim as python-base
ENV ENV=production \
    POETRY_VERSION=1.1.12 \
    PORT=8001
RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential
RUN pip install poetry
WORKDIR /app
COPY poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi
WORKDIR /app
COPY . /app
EXPOSE 8001
ENTRYPOINT /usr/local/bin/uvicorn app.main:app --host 0.0.0.0 --port $PORT
