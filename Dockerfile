FROM python:3.8-slim-buster

WORKDIR /dockerproj

COPY requirements.txt .
COPY web.py .

RUN pip install -r requirements.txt 
 

CMD ["python", "web.py"]
