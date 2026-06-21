"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#TaskStatus``."""

from typing import Literal, TypeAlias, cast

TaskStatus: TypeAlias = Literal[
    "submitted",
    "working",
    "completed",
    "canceled",
    "failed",
]


# --- restJson1 ser/de ---
def serialize_json(value: TaskStatus) -> str:
    return value


def deserialize_json(data: str) -> TaskStatus:
    return cast(TaskStatus, data)
