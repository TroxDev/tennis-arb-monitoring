

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


