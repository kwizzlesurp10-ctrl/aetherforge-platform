# ForgeMind Minimal Core Design — Phase 1

**Status:** Ready for Review
**Phase:** 1 (Minimal Closed-Loop Prototype)
**Date:** 2026-05-19
**Author:** GitHub Repository Editor Agent v2

> This document defines the smallest viable autonomous loop for ForgeMind. It has been updated with modern agent architecture pattern recommendations (hybrid OODA + ReAct, layered memory guidance).

## 1. Goals

Build the **smallest possible reliable autonomous loop** that can:
- Continuously observe the state of the repository and project
- Generate plans using a **hybrid OODA + ReAct** style cycle
- Maintain basic layered memory for decisions and learnings
- Log every decision with full provenance
- Operate in a **completely safe dry-run mode** (no modifications)

This becomes the foundation for all future autonomous capabilities.

## 2. Core Principles (Non-Negotiable)

1. **Safety First** — Planning and execution must be strictly separated.
2. **Auditability** — Every observation, decision, and plan must be logged with timestamps, reasoning, and confidence scores.
3. **Minimal Scope** — No code generation, no PR creation, no external actions in Phase 1.
4. **Observability** — Structured logging + basic cost estimation from day one.
5. **Extensibility** — Design interfaces so memory, planning, and orchestration can evolve toward hybrid patterns and sub-agent swarms.

## 3. Recommended Architecture Patterns (Phase 1+)

Based on current agentic AI research and patterns (2025–2026):

- **Primary Cognitive Loop**: Hybrid **OODA + ReAct**
  - OODA provides structured, military-grade decision making under uncertainty.
  - ReAct adds practical reasoning + tool use + observation iteration.
- **Memory Strategy**: Start simple but architected to evolve into **layered hybrid memory** (Working + Episodic + future Semantic).
- **Orchestration Approach**: Begin with a clean loop. Future phases should evaluate **graph-based state machines** (for controllability, branching, and human-in-the-loop) or **orchestrator-worker** patterns.
- **Self-Improvement Support**: Include lightweight reflection to lay groundwork for future self-mutation capabilities.

**Recommended Evolution Path**:
Simple reliable loop (Phase 1) → Graph-based or Orchestrator-Worker (Phase 4+) → Governed sub-agent swarm (Phase 5+)

## 4. High-Level Architecture (Phase 1)

```
ForgeMind Core (Dry-Run Mode)
├── Observer
│   └── Gathers repo state, issues, roadmap, design docs
├── Memory Bank (Minimal Layered)
│   ├── Working Memory (current task/context)
│   └── Episodic Store (past decisions + outcomes)
├── Planner (Hybrid OODA + ReAct)
│   ├── Observe → Orient (critique with memory)
│   ├── Decide (ranked plans + confidence)
│   ├── Act (Plan Only)
│   └── Reflect (lightweight self-evaluation)
├── Logger + Cost Tracker
│   └── Full provenance + token/cost estimation
└── Dry-Run Executor
    └── Simulates actions — never mutates anything
```

## 5. Component Breakdown

### 5.1 Observer
- Primary responsibility: Gather current project and repository state
- Sources in Phase 1:
  - Repository file structure and key files (via GitHub tools)
  - Open issues, ROADMAP, and design documents
  - Basic metadata and context
- Output: Structured context snapshot to feed the Planner

### 5.2 Evolutionary Memory Bank (Minimal — Phase 1)
**Design Philosophy**: Keep it simple and auditable today, while designing for evolution into a powerful hybrid memory system.

**Phase 1 Approach**:
- Structured JSON storage + Pydantic models
- **Working Memory**: Current task state and context
- **Episodic Memory**: History of decisions, plans, and outcomes
- Basic retrieval to support planning

**Future Direction** (Phase 2+):
- Add vector embeddings for semantic retrieval
- Introduce lightweight graph relationships
- Support memory consolidation, decay, and higher-quality retrieval

### 5.3 Planner — Hybrid OODA + ReAct Style
- **Observe**: Pull latest context from Observer + Memory Bank
- **Orient**: Critique current state against goals using memory and prompts
- **Decide**: Generate ranked plans with risk/ROI scoring and confidence levels
- **Act (Plan Only)**: Produce a detailed, reviewable action plan (never execute in Phase 1)
- **Reflect** (lightweight): Quick self-evaluation of plan quality and reasoning before finalizing

This hybrid approach combines the structured decision-making of OODA with the practical iteration of ReAct while remaining fully safe.

### 5.4 Logging & Cost Tracking
- Every cycle must produce structured, human- and machine-readable logs
- Include estimated token usage and rough cost
- Establishes the foundation for future cost control, budgeting, and governance layers

## 6. Safety & Dry-Run Mode

- **Default Mode**: Dry-run / simulation only
- Planning components generate plans but **never** invoke mutating tools or actions
- All future execution capabilities will be gated behind explicit human approval
- Logs and outputs must clearly indicate simulation mode
- Every decision must remain reviewable by humans

## 7. Technology Choices (Initial)

| Component                  | Phase 1 Recommendation              | Rationale & Future Notes |
|----------------------------|-------------------------------------|--------------------------|
| Language                   | Python 3.11+                        | Strong ecosystem for agents |
| Orchestration (Phase 1)    | Simple loop + asyncio               | Minimal dependencies, fast iteration |
| Future Orchestration       | Graph-based state machines          | Better control, branching, human-in-the-loop, auditability |
| Memory (Phase 1)           | JSON + Pydantic models              | Simple, fully auditable |
| Memory Evolution           | Hybrid Vector + Graph               | Semantic retrieval + relational knowledge |
| GitHub Integration         | Existing MCP / GitHub tools         | Already available |
| Logging                    | structlog / rich + JSON             | Structured + human readable |

## 8. Risks & Mitigations

| Risk                              | Mitigation |
|-----------------------------------|----------|
| Scope creep                       | Strict Phase 1 boundaries + narrow vertical slice |
| Over-engineering memory early     | Start minimal (JSON), evolve deliberately with clear interfaces |
| Low-quality or hallucinated plans | Structured output + confidence scoring + lightweight reflection step |
| Future difficulty evolving design | Design clean interfaces and extension points from the start |
| Cost/token issues                 | Early logging + planned budgeting layer |

## 9. Success Criteria for Phase 1

- [ ] Agent runs continuously in a stable loop
- [ ] Produces clear, auditable decision logs every cycle
- [ ] Uses basic memory to inform planning
- [ ] Generates plans referencing current issues/roadmap
- [ ] Operates fully in dry-run mode with zero side effects
- [ ] Reasoning is easy for humans to review and understand

## 10. Out of Scope (Phase 1)

- Any code changes or PR creation
- Sub-agent spawning or swarm behavior
- Real execution of plans
- Advanced self-mutation capabilities
- Production vector or graph memory systems

## 11. Next Steps After Phase 1

- Stabilize the hybrid OODA + ReAct loop with basic layered memory
- Introduce stronger human approval gates and provenance
- Evolve memory toward hybrid vector + graph capabilities
- Explore graph-based orchestration primitives for better controllability
- Proceed to Phase 2 safety hardening

---

*Living document. Updated with architecture pattern research (hybrid OODA+ReAct, layered memory, evolution path). Feedback welcome.*