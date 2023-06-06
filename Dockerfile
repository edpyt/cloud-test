FROM python:3.11.0-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /qatestapp

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY qatestcloud.py .

RUN pytest qatestcloud.py