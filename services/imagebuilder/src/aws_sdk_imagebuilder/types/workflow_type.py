"""Generated from Smithy shape ``com.amazonaws.imagebuilder#WorkflowType``."""

from typing import Literal, TypeAlias, cast

WorkflowType: TypeAlias = Literal[
    "BUILD",
    "TEST",
    "DISTRIBUTION",
]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowType) -> str:
    return value


def deserialize_json(data: str) -> WorkflowType:
    return cast(WorkflowType, data)
