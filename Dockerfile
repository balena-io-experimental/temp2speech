FROM resin/rpi-raspbian:jessie-2015-02-08

# Install Python and other dependencies
RUN apt-get update && apt-get install -y python python-dev python-pip mplayer

RUN pip install RPi.Gpio w1thermsensor

ADD . /app

CMD ["python", "/app/hello.py"]