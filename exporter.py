from flask import Flask, Response
import requests
import time
from prometheus_client import Gauge, generate_latest

app = Flask(__name__)

# Prometheus metrics
api_response_time = Gauge("external_api_response_time_seconds", "Response time of external API")
api_up = Gauge("external_api_up", "API availability status (1 = up, 0 = down)")
pm25_reading = Gauge("pm25_reading", "PM2.5 reading by region", ["region"])

API_URL = "https://api.data.gov.sg/v1/environment/pm25"

def fetch_data():
    start = time.time()
    try:
        response = requests.get(API_URL, timeout=5)
        latency = time.time() - start
        api_response_time.set(latency)

        if response.status_code == 200:
            api_up.set(1)
            data = response.json()

            readings = data["items"][0]["readings"]["pm25_one_hourly"]

            for region, value in readings.items():
                pm25_reading.labels(region=region).set(value)

        else:
            api_up.set(0)

    except Exception:
        api_up.set(0)

@app.route("/metrics")
def metrics():
    fetch_data()
    return Response(generate_latest(), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
