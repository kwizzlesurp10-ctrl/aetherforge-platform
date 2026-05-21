"""Structured Decision Logger (Interface stub)

Foundation for full auditability and cost tracking.
"""

from typing import Any


class DecisionLogger:
    """Logs every decision with provenance."""

    def log_decision(self, decision: dict[str, Any]) -> None:
        """Log a decision for auditability."""
        print(f"[ForgeMind Logger] Decision logged (dry-run): {decision.get('message', 'N/A')}")  # Temporary for scaffolding