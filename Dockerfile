FROM python:3.11-slim

LABEL author="albert"

WORKDIR /opt/app

ENV PATH="/opt/app/bin:${PATH}" \
    PYTHONPATH=/opt/app \
    PYTHONUNBUFFERED=1

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PIP_NO_CACHE_DIR=1

ENV APP_HOST="0.0.0.0"
ENV DEBUG="False"

COPY ./src .
COPY ./pyproject.toml .
COPY ./poetry.lock .

RUN pip install poetry~=1.6.1  \
    && poetry export -f requirements.txt > requirements.txt --without-hashes --without linters,typing  \
    && pip install -r requirements.txt

ENTRYPOINT ["python", "start.py"]
