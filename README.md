

A simple web tennis arbitrage model with monitoring and alerting stack
=======
# Tennis Arbitrage Monitoring Stack

Production-like monitoring and alerting stack for a web application, built with Docker, Prometheus, Blackbox Exporter, and Alertmanager.

## Overview

This project demonstrates end-to-end observability for a web service:
- **Uptime monitoring** via Blackbox Exporter HTTP probes
- **Metrics collection** via Prometheus
- **Alerting** via Alertmanager on downtime and high latency
- **Auto-recovery** via Python script that restarts the service after consecutive failures

## Architecture
┌─────────────┐     ┌─────────────────┐     ┌─────────────┐
│   nginx     │◄────│  Blackbox       │◄────│  Prometheus │
│  (web app)  │     │  Exporter       │     │             │
└─────────────┘     └─────────────────┘     └──────┬──────┘
│
┌──────▼──────┐
│ Alertmanager│
│  (alerts)   │
└─────────────┘


## Tech Stack

- **Docker & Docker Compose** — Container orchestration
- **Prometheus** — Metrics collection and alerting rules
- **Blackbox Exporter** — HTTP endpoint probing
- **Alertmanager** — Alert routing and notification
- **Nginx** — Static web server
- **Python** — Auto-restart script

## Quick Start

```bash
# Clone and start
git clone https://github.com/YOUR_USERNAME/tennis-arb-monitoring.git
cd tennis-arb-monitoring
docker compose up -d

# Access services
# Web app:      http://localhost:8080/tennis_arb.html
# Prometheus:   http://localhost:9090
# Alertmanager: http://localhost:9093

Monitoring Features

| Feature                | Implementation                                            |
| ---------------------- | --------------------------------------------------------- |
| Uptime check           | Blackbox probe every 30s                                  |
| Alert on downtime      | `probe_success == 0` for 1m                               |
| Alert on slow response | `probe_duration_seconds > 2` for 2m                       |
| Auto-restart           | Python script restarts nginx after 2 consecutive failures |

What I Learned
 - Configured multi-service Docker networks for internal communication
 - Wrote Prometheus scrape configs with relabeling for Blackbox Exporter
 - Defined alerting rules with severity levels and evaluation windows
 - Built an automated recovery mechanism to reduce manual intervention

Future Improvements
 - Grafana dashboard for visualization
 - Email/SMS notification integration
 - Multi-region probing
 - TLS/SSL certificate monitoring
>>>>>>> c763529 (initial commit: monitoring stack with prometheus, blackbox and alertmanager)
