FROM tiangolo/uwsgi-nginx-flask:python3.7

COPY . /app

COPY requirements.txt /

RUN pip install -r /requirements.txt

RUN export FLASK_APP=app