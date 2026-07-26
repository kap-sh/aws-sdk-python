"""Generated from Smithy shape ``com.amazonaws.imagebuilder#WorkflowStatus``."""

from typing import Literal, TypeAlias, cast

WorkflowStatus: TypeAlias = Literal["DEPRECATED",]


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowStatus) -> str:
    return value


def deserialize_json(data: str) -> WorkflowStatus:
    return cast(WorkflowStatus, data)
