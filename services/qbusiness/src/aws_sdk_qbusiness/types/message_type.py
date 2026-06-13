"""Generated from Smithy shape ``com.amazonaws.qbusiness#MessageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

MessageType: TypeAlias = Literal[
    "USER",
    "SYSTEM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USER",
        "SYSTEM",
    )
)


def serialize_json(value: MessageType) -> str:
    return value


def deserialize_json(data: str) -> MessageType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MessageType value: {data!r}")
    return cast(MessageType, data)
