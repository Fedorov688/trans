FROM debian
ADD . /code
WORKDIR /code
RUN apt update && \
    apt install -y python3-pip && \
    pip3 install -r requirements.txt
