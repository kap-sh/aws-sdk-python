"""Generated from Smithy shape ``com.amazonaws.imagebuilder#WorkflowStepExecutionStatus``."""

from typing import Literal, TypeAlias, cast

WorkflowStepExecutionStatus: TypeAlias = Literal[
    "PENDING",
    "SKIPPED",
    "RUNNING",
    "COMPLETED",
    "FAILED",
    "CANCELLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowStepExecutionStatus) -> str:
    return value


def deserialize_json(data: str) -> WorkflowStepExecutionStatus:
    return cast(WorkflowStepExecutionStatus, data)
