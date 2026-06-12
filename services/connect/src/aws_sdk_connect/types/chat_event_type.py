"""Generated from Smithy shape ``com.amazonaws.connect#ChatEventType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

ChatEventType: TypeAlias = Literal[
    "DISCONNECT",
    "MESSAGE",
    "EVENT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISCONNECT",
        "MESSAGE",
        "EVENT",
    )
)


def serialize_json(value: ChatEventType) -> str:
    return value


def deserialize_json(data: str) -> ChatEventType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChatEventType value: {data!r}")
    return cast(ChatEventType, data)
