# SG API Monitor — Prometheus & Grafana Demo

**Objective:**  
Monitor real-time air quality data from [data.gov.sg](https://data.gov.sg) using a custom Python exporter, Prometheus, and Grafana.

---

## Architecture

```

[data.gov.sg API]
↓
[Python Exporter] → /metrics (Prometheus format)
↓
[Prometheus] → Scrapes metrics every 15s
↓
[Grafana] → Visualizes API latency, availability & PM2.5 readings

````

**Components:**

- `exporter.py` → Calls API and exposes Prometheus metrics  
- `requirements.txt` → Python dependencies  
- `Dockerfile` → Builds exporter container  
- `prometheus.yml` → Prometheus scrape config  
- `docker-compose.yml` → Spins up exporter, Prometheus, and Grafana

---

## Setup & Run Locally

1. Clone the repo:

```bash
git clone <your-repo-url>
cd sg-api-monitor
````

2. Create a virtual environment (optional but recommended):

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Build and start containers:

```bash
docker compose up --build
```

4. Access services:

* Exporter: [http://localhost:8000/metrics](http://localhost:8000/metrics)
* Prometheus: [http://localhost:9090](http://localhost:9090)
* Grafana: [http://localhost:3000](http://localhost:3000) (admin/admin)

5. Grafana dashboard:

* Add Prometheus as data source (`http://prometheus:9090`)
* Create panels:

  * API Latency → `external_api_response_time_seconds`
  * API Availability → `external_api_up`
  * PM2.5 Reading by Region → `pm25_reading{region="..."}`

---

## Screenshots



---

## Industry Relevance

This demo mirrors real-world monitoring pipelines used in DevOps and SRE:

* Tracking external API availability and latency
* Visualizing key metrics for decision-making
* Proactively detecting SLA violations
* Containerized & scalable architecture

---

## License

````MIT License
