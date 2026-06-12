"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelMessageStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_messaging.errors import DeserializationError

ChannelMessageStatus: TypeAlias = Literal[
    "SENT",
    "PENDING",
    "FAILED",
    "DENIED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SENT",
        "PENDING",
        "FAILED",
        "DENIED",
    )
)


def serialize_json(value: ChannelMessageStatus) -> str:
    return value


def deserialize_json(data: str) -> ChannelMessageStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChannelMessageStatus value: {data!r}")
    return cast(ChannelMessageStatus, data)
