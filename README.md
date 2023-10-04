# Homework 1

A `Hello World` project. Offers API taking data from:

* query parameter
* path variable
* request body

## Quickstart

1. First of all, create `venv`:

```shell
python -m venv venv/
```

2. Create .env file in `src/`.

3. Run project either using script directly:

```shell
python src/start.py
```

or from docker:

```shell
docker build . -t homework-1 && docker run -d -p 8080:8080 --name homework-1 homework-1
```

## Linters

`black`, `isort`, `flake8`, `mypy`, `pylint` are used in this project. You can use `pre-commit` to run them all.

1. Install pre-commit into your git repository:

```shell
pre-commit install
```

2. Run hooks:

```shell
pre-commit run --all-files
```

Also, `pre-commit` runs linters just before the commit, and if a linter fails, it won't allow you to commit.

## API Documentation

To get info about API, use `/docs` url.
