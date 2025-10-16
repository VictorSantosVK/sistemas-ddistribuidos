# Monitoring (Prometheus + Grafana)

## Como rodar
```bash
docker compose up -d --build
```

Acesse:
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000  (admin / admin)
- App demo: http://localhost:8000/hello (gere tráfego)
- cAdvisor: http://localhost:8080

## Importar Dashboard
No Grafana: Dashboards → Import → Upload `grafana_dashboard.json` (desta pasta).
Selecione a datasource Prometheus quando solicitado.

## Dica Node Exporter (host)
Se o `node_exporter` não aparecer como UP, instale/rode localmente: 
```bash
docker run -d --name node_exporter --net=host --pid=host prom/node-exporter:v1.8.1
```
E mantenha no `prometheus.yml` o alvo `localhost:9100`.
