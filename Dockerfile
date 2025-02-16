FROM python:3.12

WORKDIR /app

COPY requirements.txt . 

RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app
 # Copy all files from the current directory to the container

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]