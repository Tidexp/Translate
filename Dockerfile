FROM libretranslate/libretranslate:latest

RUN pip install argostranslate

COPY vi /app/vi

RUN python3 /app/vi/install.py

CMD libretranslate
