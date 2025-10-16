FROM python:3.11-slim
WORKDIR /app
COPY server.py /app/server.py
RUN pip install --no-cache-dir flask prometheus-client
ENV PORT=8000
CMD ["python", "server.py"]
