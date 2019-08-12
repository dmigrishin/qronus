from alpine:latest

FROM alpine:3.10

RUN apk add --no-cache python && \
    python -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip install --upgrade pip setuptools && \
    rm -r /root/.cache

WORKDIR /app

COPY . /app

RUN pip install google-auth requests enum

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["main.py"]