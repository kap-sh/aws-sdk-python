"""Generated from Smithy shape ``com.amazonaws.imagebuilder#WorkflowExecutionStatus``."""

from typing import Literal, TypeAlias, cast

WorkflowExecutionStatus: TypeAlias = Literal[
    "PENDING",
    "SKIPPED",
    "RUNNING",
    "COMPLETED",
    "FAILED",
    "ROLLBACK_IN_PROGRESS",
    "ROLLBACK_COMPLETED",
    "CANCELLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> WorkflowExecutionStatus:
    return cast(WorkflowExecutionStatus, data)
