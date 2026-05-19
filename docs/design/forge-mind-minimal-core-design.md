# ForgeMind Minimal Core Design — Phase 1

**Status:** Draft — For Discussion
**Phase:** 1 (Minimal Closed-Loop Prototype)
**Date:** 2026-05-19
**Author:** GitHub Repository Editor Agent v2

## 1. Goals

Build the **smallest possible reliable autonomous loop** that can:
- Continuously observe the state of the repository and project
- Generate plans using an OODA-style cycle
- Log every decision with full provenance
- Operate in a **completely safe dry-run mode** (no modifications)

This becomes the foundation for all future autonomous capabilities.

## 2. Core Principles (Non-Negotiable)

1. **Safety First** — Planning and execution must be strictly separated.
2. **Auditability** — Every observation, decision, and plan must be logged with timestamps, reasoning, and confidence scores.
3. **Minimal Scope** — No code generation, no PR creation, no external actions in Phase 1.
4. **Observability** — Structured logging + basic cost estimation from day one.
5. **Extensibility** — Design memory and planning interfaces so they can evolve.

## 3. High-Level Architecture (Phase 1)

```
ForgeMind Core
├── Observer          # Reads repo state, issues, metrics
├── Memory Bank       # Simple persistent storage (start with JSON + optional vector)
├── Planner (OODA)    # Observe → Orient → Decide → Act (plan only)
├── Logger            # Structured decision + cost logging
└── Dry-Run Executor  # Simulates actions, never executes
```

## 4. Component Breakdown

### 4.1 Observer
- Primary responsibility: Gather current state
- Sources (Phase 1):
  - Repository file tree (via GitHub tools)
  - Open issues and roadmap
  - Basic code analysis (future)
- Output: Structured context snapshot

### 4.2 Evolutionary Memory Bank (Minimal)
- Start simple: File-based JSON store + optional local vector (Chroma or similar)
- Stores:
  - Past decisions and outcomes
  - Plans and their evaluations
  - Lessons learned
- Must support basic retrieval for planning

### 4.3 OODA Planning Engine
- **Observe**: Pull latest context from Observer + Memory
- **Orient**: Critique current state vs goals (using prompts + memory)
- **Decide**: Generate ranked plans with risk/ROI scoring
- **Act (Plan Only)**: Output a detailed action plan (never execute in Phase 1)

### 4.4 Logging & Cost Tracking
- Every cycle must produce structured logs
- Include estimated token usage and rough cost
- Foundation for future budgeting and runaway prevention

## 5. Safety & Dry-Run Mode

- **Default Mode**: Dry-run only
- All "Act" steps generate plans but do **not** call any mutating tools
- Future execution layer will sit behind explicit human approval gates
- Clear visual/CLI indication that the agent is in simulation mode

## 6. Technology Choices (Initial)

| Component          | Recommended Starting Choice      | Rationale |
|--------------------|----------------------------------|---------|
| Language           | Python 3.11+                     | Strong agent ecosystem, aligns with FastAPI vision |
| Orchestration      | Simple `while True` loop + asyncio | Minimal dependencies |
| Memory             | JSON files + pydantic models     | Simple, auditable, easy to evolve |
| Vector (optional)  | Chroma (local) or pgvector       | Easy local start |
| GitHub Integration | Existing MCP / GitHub tools      | Already connected |
| Logging            | structlog or rich + JSON         | Structured and human readable |

## 7. Risks & Mitigations

| Risk                        | Mitigation |
|-----------------------------|----------|
| Scope creep                 | Strict Phase 1 definition + narrow vertical slice |
| Over-engineering memory     | Start with JSON, evolve later |
| Hallucinated plans          | Require structured output + confidence scoring |
| Cost explosion              | Logging + future budgeting layer |

## 8. Success Criteria for Phase 1

- [ ] Agent runs in a continuous loop without crashing
- [ ] Produces auditable decision logs every cycle
- [ ] Generates plans that reference current issues/roadmap
- [ ] Clearly operates in dry-run mode
- [ ] Easy to review logs and understand reasoning

## 9. Out of Scope (Phase 1)

- Any code modification
- PR creation
- Sub-agent spawning
- Real execution of plans
- Self-improvement of the agent

## 10. Next Steps After Phase 1

- Stabilize core loop
- Add human approval UI/gates
- Expand memory sophistication
- Move to Phase 2 safety hardening

---

*This is a living design document. Feedback welcome.*