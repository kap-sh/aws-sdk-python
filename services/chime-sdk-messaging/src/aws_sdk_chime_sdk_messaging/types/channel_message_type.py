"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelMessageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_messaging.errors import DeserializationError

ChannelMessageType: TypeAlias = Literal[
    "STANDARD",
    "CONTROL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD",
        "CONTROL",
    )
)


def serialize_json(value: ChannelMessageType) -> str:
    return value


def deserialize_json(data: str) -> ChannelMessageType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChannelMessageType value: {data!r}")
    return cast(ChannelMessageType, data)
