"""Generated from Smithy shape ``com.amazonaws.pinpoint#MessageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pinpoint.errors import DeserializationError

MessageType: TypeAlias = Literal[
    "TRANSACTIONAL",
    "PROMOTIONAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TRANSACTIONAL",
        "PROMOTIONAL",
    )
)


def serialize_json(value: MessageType) -> str:
    return value


def deserialize_json(data: str) -> MessageType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MessageType value: {data!r}")
    return cast(MessageType, data)
