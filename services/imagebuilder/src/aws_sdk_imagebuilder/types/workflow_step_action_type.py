"""Generated from Smithy shape ``com.amazonaws.imagebuilder#WorkflowStepActionType``."""

from typing import Literal, TypeAlias, cast

WorkflowStepActionType: TypeAlias = Literal[
    "RESUME",
    "STOP",
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowStepActionType) -> str:
    return value


def deserialize_json(data: str) -> WorkflowStepActionType:
    return cast(WorkflowStepActionType, data)
