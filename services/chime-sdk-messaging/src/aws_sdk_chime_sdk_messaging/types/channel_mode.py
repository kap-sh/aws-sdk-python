"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_messaging.errors import DeserializationError

ChannelMode: TypeAlias = Literal[
    "UNRESTRICTED",
    "RESTRICTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNRESTRICTED",
        "RESTRICTED",
    )
)


def serialize_json(value: ChannelMode) -> str:
    return value


def deserialize_json(data: str) -> ChannelMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChannelMode value: {data!r}")
    return cast(ChannelMode, data)
