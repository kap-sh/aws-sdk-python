"""Generated from Smithy shape ``com.amazonaws.polly#TaskStatus``."""

from typing import Literal, TypeAlias, cast

TaskStatus: TypeAlias = Literal[
    "scheduled",
    "inProgress",
    "completed",
    "failed",
]


# --- restJson1 ser/de ---
def serialize_json(value: TaskStatus) -> str:
    return value


def deserialize_json(data: str) -> TaskStatus:
    return cast(TaskStatus, data)
