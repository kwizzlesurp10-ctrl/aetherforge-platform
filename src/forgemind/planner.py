"""OODA Planning Engine (Interface stub)

Generates plans but does not execute them in Phase 1.
"""

from typing import Any


class Planner:
    """Generates ranked plans from observations."""

    def generate_plan(self, observation: dict[str, Any]) -> dict[str, Any]:
        """Generate a plan (dry-run / simulation only)."""
        return {
            "plan": "stub_plan",
            "confidence": 0.0,
            "dry_run": True,
            "message": "Planner interface - returns stub plan only",
        }