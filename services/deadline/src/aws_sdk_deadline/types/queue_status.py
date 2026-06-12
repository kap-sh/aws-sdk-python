"""Generated from Smithy shape ``com.amazonaws.deadline#QueueStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

QueueStatus: TypeAlias = Literal[
    "IDLE",
    "SCHEDULING",
    "SCHEDULING_BLOCKED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IDLE",
        "SCHEDULING",
        "SCHEDULING_BLOCKED",
    )
)


def serialize_json(value: QueueStatus) -> str:
    return value


def deserialize_json(data: str) -> QueueStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QueueStatus value: {data!r}")
    return cast(QueueStatus, data)
