from flask import Flask, Response, request
from prometheus_client import Counter, Histogram, generate_latest


app = Flask(__name__)


# Nous definissons les metriques que nous souhaitons exporter
REQUEST_COUNT = Counter('http_request_count', 'Total HTTP Request Count', ['method', 'endpoint', 'ip']) # Un Compteur pour le nombre de requetes
REQUEST_LATENCY = Histogram('http_request_latency_seconds', 'HTTP Request Latency', ['method', 'endpoint']) # Un Histogramme pour la latence des requetes
ARTICLE_COUNT = Counter('article_count', 'Total posted article Count', ['id']) # Un Compteur pour le nombre d'articles postés


@app.before_request
def before_monitoring():
    REQUEST_COUNT.labels(method=request.method, endpoint=request.endpoint, ip=request.remote_addr).inc() # On incremente le compteur de requetes à chaque requete

@app.route('/')
def hello():
    with REQUEST_LATENCY.labels(method=request.method, endpoint=request.endpoint).time(): # On mesure la latence de la requete
        return 'Hello, World!'


@app.route('/articles', methods=["POST"])
def add_article():
    with REQUEST_LATENCY.labels(method=request.method, endpoint=request.endpoint).time():
        return 'Hello, World!'


# Nous definissons une route pour exporter les metriques
@app.route('/metrics')
def metrics():
    resp = Response(generate_latest())
    resp.headers['Content-type'] = 'text/plain; version=0.0.4; charset=utf-8'
    return resp



if __name__ == '__main__':
  app.run(debug=True)