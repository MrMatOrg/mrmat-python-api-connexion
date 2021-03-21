FROM python:3.9.2-alpine3.13

ADD requirements.txt /
COPY dist/mrmat-python-flask-api-*.tar.gz /
RUN \
    pip install -r /requirements.txt \
    && pip install /mrmat-python-flask-api-*.tar.gz \
    && rm -f /requirements.txt /mrmat-python-flask-api-*.tar.gz

USER 1000:1000
EXPOSE 8080
ENTRYPOINT mrmat-python-flask-api --host 0.0.0.0
