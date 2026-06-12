"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#MessagingDataType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_messaging.errors import DeserializationError

MessagingDataType: TypeAlias = Literal[
    "Channel",
    "ChannelMessage",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Channel",
        "ChannelMessage",
    )
)


def serialize_json(value: MessagingDataType) -> str:
    return value


def deserialize_json(data: str) -> MessagingDataType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MessagingDataType value: {data!r}")
    return cast(MessagingDataType, data)
