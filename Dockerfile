FROM python:3.9

SHELL ["/bin/bash", "-c"] 

ADD . /api
RUN chmod -R 765 /api

WORKDIR /api

RUN pip install virtualenv
RUN virtualenv venv
RUN source venv/bin/activate
RUN pip install -r requirements.txt

CMD gunicorn -w 2 --threads 2 -b 0.0.0.0:8080 server:app