"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelMembershipType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_messaging.errors import DeserializationError

ChannelMembershipType: TypeAlias = Literal[
    "DEFAULT",
    "HIDDEN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEFAULT",
        "HIDDEN",
    )
)


def serialize_json(value: ChannelMembershipType) -> str:
    return value


def deserialize_json(data: str) -> ChannelMembershipType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChannelMembershipType value: {data!r}")
    return cast(ChannelMembershipType, data)
