"""Generated from Smithy shape ``com.amazonaws.medialive#LinkedChannelType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""The values for the role for a linked channel."""
LinkedChannelType: TypeAlias = Literal[
    "FOLLOWING_CHANNEL",
    "PRIMARY_CHANNEL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FOLLOWING_CHANNEL",
        "PRIMARY_CHANNEL",
    )
)


def serialize_json(value: LinkedChannelType) -> str:
    return value


def deserialize_json(data: str) -> LinkedChannelType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LinkedChannelType value: {data!r}")
    return cast(LinkedChannelType, data)
