"""Generated from Smithy shape ``com.amazonaws.ivs#ChannelType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ivs.errors import DeserializationError

ChannelType: TypeAlias = Literal[
    "BASIC",
    "STANDARD",
    "ADVANCED_SD",
    "ADVANCED_HD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BASIC",
        "STANDARD",
        "ADVANCED_SD",
        "ADVANCED_HD",
    )
)


def serialize_json(value: ChannelType) -> str:
    return value


def deserialize_json(data: str) -> ChannelType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChannelType value: {data!r}")
    return cast(ChannelType, data)
