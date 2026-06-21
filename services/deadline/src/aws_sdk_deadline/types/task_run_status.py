"""Generated from Smithy shape ``com.amazonaws.deadline#TaskRunStatus``."""

from typing import Literal, TypeAlias, cast

TaskRunStatus: TypeAlias = Literal[
    "PENDING",
    "READY",
    "ASSIGNED",
    "STARTING",
    "SCHEDULED",
    "INTERRUPTING",
    "RUNNING",
    "SUSPENDED",
    "CANCELED",
    "FAILED",
    "SUCCEEDED",
    "NOT_COMPATIBLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: TaskRunStatus) -> str:
    return value


def deserialize_json(data: str) -> TaskRunStatus:
    return cast(TaskRunStatus, data)
