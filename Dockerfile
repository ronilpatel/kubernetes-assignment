FROM python:3.9-slim-buster

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install -r requirements.txt

COPY . .

EXPOSE 9999

ENV FLASK_APP=app.py

#CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5050"]
CMD ["python3", "-u", "-m", "flask", "run", "--host=0.0.0.0"]