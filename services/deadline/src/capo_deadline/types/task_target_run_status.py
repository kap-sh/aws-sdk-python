"""Generated from Smithy shape ``com.amazonaws.deadline#TaskTargetRunStatus``."""

from typing import Literal, TypeAlias, cast

TaskTargetRunStatus: TypeAlias = Literal[
    "READY",
    "FAILED",
    "SUCCEEDED",
    "CANCELED",
    "SUSPENDED",
    "PENDING",
]


# --- restJson1 ser/de ---
def serialize_json(value: TaskTargetRunStatus) -> str:
    return value


def deserialize_json(data: str) -> TaskTargetRunStatus:
    return cast(TaskTargetRunStatus, data)
