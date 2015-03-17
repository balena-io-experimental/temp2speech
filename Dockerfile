FROM resin/rpi-raspbian:wheezy-2015-01-15

# Install Python.
RUN apt-get update && apt-get install -y python python-dev python-pip mplayer

RUN pip install RPi.Gpio w1thermsensor

ADD . /app

CMD ["python", "/app/hello.py"]