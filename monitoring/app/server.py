import os, random, time
from flask import Flask, jsonify
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUESTS = Counter(
    "app_http_requests_total",
    "Total de requisições HTTP",
    ["method", "endpoint", "code"]
)
REQ_LATENCY = Histogram(
    "app_request_duration_seconds",
    "Duração das requisições",
    ["endpoint"],
    buckets=[0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5]
)
ERRORS = Counter(
    "app_http_errors_total",
    "Total de erros 5xx",
    ["endpoint"]
)

@app.route("/hello")
def hello():
    start = time.time()
    time.sleep(random.uniform(0.01, 0.2))
    if random.random() < 0.05:
        ERRORS.labels(endpoint="/hello").inc()
        REQUESTS.labels(method="GET", endpoint="/hello", code="500").inc()
        return jsonify({"error": "internal"}), 500
    REQUESTS.labels(method="GET", endpoint="/hello", code="200").inc()
    REQ_LATENCY.labels(endpoint="/hello").observe(time.time() - start)
    return jsonify({"message": "world"})

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    app.run(host="0.0.0.0", port=port)
