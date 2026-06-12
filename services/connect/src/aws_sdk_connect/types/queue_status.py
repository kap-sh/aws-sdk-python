"""Generated from Smithy shape ``com.amazonaws.connect#QueueStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

QueueStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: QueueStatus) -> str:
    return value


def deserialize_json(data: str) -> QueueStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown QueueStatus value: {data!r}")
    return cast(QueueStatus, data)
