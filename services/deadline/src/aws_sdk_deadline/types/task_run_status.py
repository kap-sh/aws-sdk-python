"""Generated from Smithy shape ``com.amazonaws.deadline#TaskRunStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: TaskRunStatus) -> str:
    return value


def deserialize_json(data: str) -> TaskRunStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaskRunStatus value: {data!r}")
    return cast(TaskRunStatus, data)
