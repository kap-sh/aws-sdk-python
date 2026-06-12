"""Generated from Smithy shape ``com.amazonaws.connect#QueueType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

QueueType: TypeAlias = Literal[
    "STANDARD",
    "AGENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD",
        "AGENT",
    )
)


def serialize_json(value: QueueType) -> str:
    return value


def deserialize_json(data: str) -> QueueType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QueueType value: {data!r}")
    return cast(QueueType, data)
