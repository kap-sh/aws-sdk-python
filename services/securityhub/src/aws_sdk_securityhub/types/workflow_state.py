"""Generated from Smithy shape ``com.amazonaws.securityhub#WorkflowState``."""

from typing import Literal, TypeAlias, cast

WorkflowState: TypeAlias = Literal[
    "NEW",
    "ASSIGNED",
    "IN_PROGRESS",
    "DEFERRED",
    "RESOLVED",
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowState) -> str:
    return value


def deserialize_json(data: str) -> WorkflowState:
    return cast(WorkflowState, data)
