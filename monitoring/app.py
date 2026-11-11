from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

requests = Counter(
    'app_requests_total', 
    'Total requests'
)

@app.route('/')
def home():
    requests.inc()
    return "Welcome to flask app!"

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

app.run(host='0.0.0.0', port=5000)
