"""Generated from Smithy shape ``com.amazonaws.tnb#TaskStatus``."""

from typing import Literal, TypeAlias, cast

TaskStatus: TypeAlias = Literal[
    "SCHEDULED",
    "STARTED",
    "IN_PROGRESS",
    "COMPLETED",
    "ERROR",
    "SKIPPED",
    "CANCELLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: TaskStatus) -> str:
    return value


def deserialize_json(data: str) -> TaskStatus:
    return cast(TaskStatus, data)
