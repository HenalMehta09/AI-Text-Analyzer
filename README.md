# AI Text Analyzer — DevOps Project

This project demonstrates an end-to-end DevOps workflow by deploying a simple AI-based text analysis application using modern cloud-native tools.

## 🧠 What the App Does

Users enter text in a web UI.  
The application analyzes the sentiment using a lightweight AI service.

**Flow:**
Frontend → Backend API → AI Service → Response

## 🏗 Architecture

- **Frontend**: Static HTML + JS (served via Nginx)
- **Backend**: FastAPI service
- **AI Service**: FastAPI-based text sentiment analyzer
- **Containerization**: Docker
- **CI/CD**: GitHub Actions
- **Image Registry**: AWS ECR
- **Orchestration**: Kubernetes (planned)
- **Packaging**: Helm (planned)
- **Infrastructure**: Terraform (planned)

## 📦 Services

| Service | Port | Description |
|------|------|------------|
| frontend | 80 | Web UI |
| backend | 8000 | API gateway |
| ai-service | 8001 | Text analysis engine |

## 🚀 CI/CD Pipeline

- On every push to `main`:
  - Build Docker images
  - Push images to AWS ECR

## 🔐 Secrets Handling

All sensitive values (AWS credentials) are stored securely using **GitHub Actions Secrets**.

## 📌 Future Improvements

- Terraform-managed AWS infrastructure
- Kubernetes (EKS) deployment
- Helm charts for services
- Ingress with HTTPS
- Observability (Prometheus + Grafana)

## 👤 Author

Built by **Henal Mehta** as a hands-on DevOps learning project.
