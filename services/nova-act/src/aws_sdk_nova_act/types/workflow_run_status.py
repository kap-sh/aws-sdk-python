"""Generated from Smithy shape ``com.amazonaws.novaact#WorkflowRunStatus``."""

from typing import Literal, TypeAlias, cast

WorkflowRunStatus: TypeAlias = Literal[
    "RUNNING",
    "SUCCEEDED",
    "FAILED",
    "TIMED_OUT",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowRunStatus) -> str:
    return value


def deserialize_json(data: str) -> WorkflowRunStatus:
    return cast(WorkflowRunStatus, data)
