FROM python:3.7.8-slim-stretch

# dont write pyc files
# dont buffer to stdout/stderr
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code
WORKDIR /code/
RUN mkdir -p /code/package
RUN pwd

COPY requirements.txt /code/
COPY /package/ /code/package/

# dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir --upgrade pip setuptools wheel \
    && pip install -r requirements.txt \
    && rm -rf /root/.cache/pip

RUN apt-get update && apt-get install -y procps libsm6 libxext6 libxrender-dev libglib2.0-0 git

COPY . /code/

CMD ["streamlit", "run", "app.py", "--server.port", "8501"]