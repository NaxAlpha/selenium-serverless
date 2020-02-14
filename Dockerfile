FROM python:3.7
RUN apt update && apt install -y chromium-driver
RUN pip install selenium flask
ADD . /app
WORKDIR /app
CMD python app.py
