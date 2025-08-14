FROM libretranslate/libretranslate:latest

# Cập nhật repo và cài pip nếu chưa có
RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip3 install --upgrade pip

RUN pip3 install argostranslate

COPY vi /app/vi

RUN python3 /app/vi/install.py

CMD libretranslate
