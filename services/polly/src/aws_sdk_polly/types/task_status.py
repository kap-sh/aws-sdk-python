"""Generated from Smithy shape ``com.amazonaws.polly#TaskStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_polly.errors import DeserializationError

TaskStatus: TypeAlias = Literal[
    "scheduled",
    "inProgress",
    "completed",
    "failed",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "scheduled",
        "inProgress",
        "completed",
        "failed",
    )
)


def serialize_json(value: TaskStatus) -> str:
    return value


def deserialize_json(data: str) -> TaskStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TaskStatus value: {data!r}")
    return cast(TaskStatus, data)
