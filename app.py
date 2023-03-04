from flask import Flask, Response
from prometheus_client import Counter, Histogram, generate_latest

app = Flask(__name__)


REQUEST_COUNT = Counter('http_request_count', 'Total HTTP Request Count', ['method', 'endpoint'])
REQUEST_LATENCY = Histogram('http_request_latency_seconds', 'HTTP Request Latency', ['method', 'endpoint'])

@app.route('/')
def hello():
    REQUEST_COUNT.labels(method='GET', endpoint='/').inc()
    with REQUEST_LATENCY.labels(method='GET', endpoint='/').time():
        return 'Hello, World!'

@app.route('/metrics')
def metrics():
    resp = Response(generate_latest())
    resp.headers['Content-type'] = 'text/plain; version=0.0.4; charset=utf-8'
    return resp