"""Generated from Smithy shape ``com.amazonaws.mediaconvert#QueueStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Queues can be ACTIVE or PAUSED. If you pause a queue, jobs in that queue won't begin. Jobs that are running when you pause a queue continue to run until they finish or result in an error."""
QueueStatus: TypeAlias = Literal[
    "ACTIVE",
    "PAUSED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "PAUSED",
    )
)


def serialize_json(value: QueueStatus) -> str:
    return value


def deserialize_json(data: str) -> QueueStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QueueStatus value: {data!r}")
    return cast(QueueStatus, data)
