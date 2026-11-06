# DevOps-Lab3

**Course:** DevOps and Automation
Monitoring, Logging & DevSecOps

This repository contains the code, configuration files and results for Lab 3. Each task has its own folder.

## Tasks

| Task | Folder | What it does |
|------|--------|--------------|
| 1. Configure infrastructure and automate application | `task1/` | Ansible playbook that installs nginx and deploys a web page |
| 2. Provision scalable infrastructure | `task2/` | Terraform (Docker provider) creating and scaling nginx containers |
| 3. Implement centralized logging | `task3/` | ELK stack (Elasticsearch, Logstash, Kibana) with a grok pipeline |
| 4. Integrate security into the CI/CD pipeline | `task4/`, `.github/workflows/` | GitHub Actions workflow that scans dependencies with pip-audit on every push |
| 5. Set up monitoring using Prometheus | `task5/` | Prometheus, Node Exporter and Grafana with Docker Compose |
| 6. Feature flags and testing | `task6/` | Flask feature flag, ApacheBench load test and Selenium test |
| 7. Monitoring, logging and DevSecOps report | `task7/` | Final report with screenshots |

## How to run each task

**Task 1 (Ansible)**
```bash
cd task1
ansible-playbook -i inventory.ini playbook.yml
curl localhost
```

**Task 2 (Terraform)**
```bash
cd task2
terraform init
terraform plan
terraform apply -auto-approve
docker ps
```

**Task 3 (ELK)**
```bash
cd task3
docker compose up -d
# Kibana: http://localhost:5601
```

**Task 4 (DevSecOps)**
The workflow `.github/workflows/security.yml` runs automatically on every push. Results are in the repository's Actions tab.

**Task 5 (Prometheus and Grafana)**
```bash
cd task5
docker compose up -d
# Prometheus: http://localhost:9090   Grafana: http://localhost:3000
```

**Task 6 (Feature flag, load test, Selenium)**
```bash
cd task6
NEW_FEATURE=on python3 app.py
ab -n 1000 -c 50 http://localhost:5000/
python3 test.py
```

## Tools used
Ansible, Terraform, Docker and Docker Compose, Elasticsearch/Logstash/Kibana 8.13.4, Prometheus, Node Exporter, Grafana, GitHub Actions, pip-audit, Flask, ApacheBench, Selenium.

## Environment
Windows with WSL2 (Ubuntu 24.04) and Docker Desktop.
