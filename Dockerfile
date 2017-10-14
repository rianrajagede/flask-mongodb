FROM ubuntu:16.04

RUN apt-get update -y
RUN apt-get install -y python3 python3-pip python3-dev build-essential libssl-dev libffi-dev

COPY . /app

WORKDIR /app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD ["python3", "run.py"]
