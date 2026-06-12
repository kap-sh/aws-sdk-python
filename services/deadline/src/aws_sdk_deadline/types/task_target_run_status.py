"""Generated from Smithy shape ``com.amazonaws.deadline#TaskTargetRunStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

TaskTargetRunStatus: TypeAlias = Literal[
    "READY",
    "FAILED",
    "SUCCEEDED",
    "CANCELED",
    "SUSPENDED",
    "PENDING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "READY",
        "FAILED",
        "SUCCEEDED",
        "CANCELED",
        "SUSPENDED",
        "PENDING",
    )
)


def serialize_json(value: TaskTargetRunStatus) -> str:
    return value


def deserialize_json(data: str) -> TaskTargetRunStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaskTargetRunStatus value: {data!r}")
    return cast(TaskTargetRunStatus, data)
