FROM python:3.8.10-slim
COPY . /app
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
RUN apt update -y
RUN apt --yes install libsndfile1-dev

EXPOSE 8000
CMD  uvicorn app.main:app --host 0.0.0.0 --port 8000