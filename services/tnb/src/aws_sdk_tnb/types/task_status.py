"""Generated from Smithy shape ``com.amazonaws.tnb#TaskStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_tnb.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "SCHEDULED",
        "STARTED",
        "IN_PROGRESS",
        "COMPLETED",
        "ERROR",
        "SKIPPED",
        "CANCELLED",
    )
)


def serialize_json(value: TaskStatus) -> str:
    return value


def deserialize_json(data: str) -> TaskStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaskStatus value: {data!r}")
    return cast(TaskStatus, data)
