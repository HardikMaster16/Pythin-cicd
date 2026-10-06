from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
 
app = Flask(__name__)
metrics = PrometheusMetrics(app)  # adds /metrics automatically
 
 
def greet(name):
    return f"Hello, {name}!"
 
 
@app.get("/")
def home():
    return jsonify(message="CI/CD demo is running")
 
 
@app.get("/health")
def health():
    return jsonify(status="ok")
 
 
@app.get("/greet/<name>")
def greet_route(name):
    return jsonify(message=greet(name))
 
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
