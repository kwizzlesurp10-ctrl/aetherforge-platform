"""Observer component (Interface stub)

Responsible for gathering current repository and project state.
"""

from typing import Any


class Observer:
    """Gathers context from the repository and environment."""

    def observe(self) -> dict[str, Any]:
        """Return structured observation of current state."""
        # TODO: Implement using GitHub tools in future phase
        return {
            "status": "stub",
            "message": "Observer interface - not yet implemented",
        }