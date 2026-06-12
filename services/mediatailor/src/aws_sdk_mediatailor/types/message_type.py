"""Generated from Smithy shape ``com.amazonaws.mediatailor#MessageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediatailor.errors import DeserializationError

MessageType: TypeAlias = Literal[
    "SPLICE_INSERT",
    "TIME_SIGNAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SPLICE_INSERT",
        "TIME_SIGNAL",
    )
)


def serialize_json(value: MessageType) -> str:
    return value


def deserialize_json(data: str) -> MessageType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MessageType value: {data!r}")
    return cast(MessageType, data)
