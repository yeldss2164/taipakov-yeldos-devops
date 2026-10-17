FROM python:3.11-slim

WORKDIR /app

COPY app/ .

RUN python -m compileall -q .

EXPOSE 5000

CMD ["python", "-u", "app.py"]
