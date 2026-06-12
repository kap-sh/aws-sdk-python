"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelPrivacy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_messaging.errors import DeserializationError

ChannelPrivacy: TypeAlias = Literal[
    "PUBLIC",
    "PRIVATE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUBLIC",
        "PRIVATE",
    )
)


def serialize_json(value: ChannelPrivacy) -> str:
    return value


def deserialize_json(data: str) -> ChannelPrivacy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChannelPrivacy value: {data!r}")
    return cast(ChannelPrivacy, data)
