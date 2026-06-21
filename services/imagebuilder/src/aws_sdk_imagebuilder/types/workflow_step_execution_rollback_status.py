"""Generated from Smithy shape ``com.amazonaws.imagebuilder#WorkflowStepExecutionRollbackStatus``."""

from typing import Literal, TypeAlias, cast

WorkflowStepExecutionRollbackStatus: TypeAlias = Literal[
    "RUNNING",
    "COMPLETED",
    "SKIPPED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowStepExecutionRollbackStatus) -> str:
    return value


def deserialize_json(data: str) -> WorkflowStepExecutionRollbackStatus:
    return cast(WorkflowStepExecutionRollbackStatus, data)
