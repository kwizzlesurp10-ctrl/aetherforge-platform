# AetherForge

**The Autonomous Full-Stack Software Factory**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**A production-grade, self-evolving full-stack platform engineered as a self-evolving software factory. At its core resides ForgeMind, a persistent autonomous agent that operates as a background process to continuously plan, architect, implement, test, deploy, and iterate on the entire system.**

Built for developers, startups, and enterprises who want AI that doesn’t just *assist* — it **owns** the entire software lifecycle.

## ✨ Features

- **ForgeMind Autonomous Agent** – Persistent background daemon that runs OODA loops, decomposes tasks, generates code, creates PRs, monitors metrics, and evolves the system without human intervention.
- **True Full-Stack Generation** – Frontend (Next.js 15), Backend (NestJS + FastAPI hybrid), Database (PostgreSQL + Neo4j + Vector), Infra (Kubernetes + Terraform), CI/CD, and Observability — all agent-driven.
- **Hierarchical Planning Engine** – Real-time Failure Heat Map, risk scoring, and self-mutating agent swarm.
- **Human-in-the-Loop + Full Autonomy Modes** – Natural language commands, visual canvas integration, or completely hands-off evolution.
- **Enterprise-Grade Observability** – OpenTelemetry, live system mirror, audit trails, and provenance for every generated line of code.
- **Self-Improving Memory** – Vector + Graph knowledge store + Evolutionary Memory Bank that learns from every cycle.
- **Open & Extensible** – Fully open-source core, plugin system for custom sub-agents.

## 📈 Architecture

```mermaid
flowchart TD
    subgraph "Human / Stakeholder Interfaces"
        A[Natural Language Studio] 
        B[Visual Canvas (Tldraw)]
        C[Live System Mirror]
    end

    subgraph "ForgeMind Core (Background Daemon Cluster)"
        D[Central Coordinator]
        E[Planning Engine + OODA]
        F[Sub-Agent Swarm\n(Architect • Security • UX • Perf • Cost)]
        G[Evolutionary Memory Bank + Knowledge Graph]
        H[Realignment Critic + Failure Heat Map]
    end

    subgraph "Full-Stack Runtime"
        I[Frontend: Next.js 15 + React 19]
        J[Backend: NestJS + FastAPI + Temporal.io]
        K[Data: PostgreSQL + Neo4j + pgvector + Redis]
        L[Infra: Kubernetes + ArgoCD + Terraform]
        M[Observability: OpenTelemetry + Grafana]
    end

    A & B & C --> D
    D <--> E <--> F <--> G <--> H
    D --> I & J & K & L & M
    style D fill:#22c55e,stroke:#000
```

**Core Philosophy**: Software development is no longer a project — it’s a living, continuously optimized organism.

## 🛠 Tech Stack

| Layer              | Technology |
|--------------------|----------|
| **Frontend**       | Next.js 15 (App Router), React 19, TypeScript, Tailwind, shadcn/ui, TanStack Query |
| **Backend**        | NestJS (TypeScript) + FastAPI (Python) microservices, Temporal.io workflows |
| **Data**           | PostgreSQL (PostGIS + Timescale + pgvector), Redis, Neo4j, Pinecone |
| **Agent Orchestration** | Ray / Modal + custom MCP/A2A/ACP protocols |
| **Infra & DevOps** | Kubernetes, Terraform/Pulumi, ArgoCD, GitHub Actions |
| **Observability**  | OpenTelemetry, Prometheus, Grafana, Loki |
| **Security**       | OAuth2/OIDC, mTLS, automated SAST/DAST |

## 🚀 Quick Start (Self-Hosting)

```bash
# 1. Clone the repo
git clone https://github.com/kwizzlesurp10-ctrl/aetherforge-platform.git
cd aetherforge-platform

# 2. Start the full stack + ForgeMind in one command
docker compose up -d --build

# 3. Open the studio
open http://localhost:3000
```

**First interaction**:
Type in the chat:  
`"Initialize a SaaS product with user auth, payments, and AI recommendations"`

ForgeMind will immediately begin planning, building, and deploying — in the background.

### Prerequisites
- Docker + Docker Compose
- Optional: Kubernetes cluster for production-scale ForgeMind

## 🧬 How ForgeMind Works (Autonomous Background Process)

1. **Sense** – Continuously monitors repo, metrics, logs, user input, and external signals.
2. **Orient** – Analyzes state against goals using specialized critics.
3. **Decide** – Generates versioned plans with risk scores and predicted ROI.
4. **Act** – Executes changes via sandboxed codegen → automated PRs → preview environments → tests → deployment.
5. **Learn** – Logs every delta to the Evolutionary Memory Bank.

Runs 24/7. Never sleeps. Improves with every cycle.

## 🛣 Roadmap (Community Driven)

- [x] v1.0 – Core ForgeMind + Full-Stack Generation
- [ ] v1.1 – Multi-tenant SaaS templates + Marketplace for agent plugins
- [ ] v1.2 – Visual architecture-to-code canvas (drag & drop → live app)
- [ ] v2.0 – Decentralized agent swarm

See ROADMAP.md for full details.

## 🤝 Contributing

We believe the future of software should be built **in public** by the community.

See [CONTRIBUTING.md](CONTRIBUTING.md)

## 📄 License

**MIT License** – See [LICENSE](LICENSE) file.

---

**Made with ❤️ by the Elite Agent Agency and the open-source community.**

**Repo**: https://github.com/kwizzlesurp10-ctrl/aetherforge-platform
