"""Generated from Smithy shape ``com.amazonaws.ivs#ChannelType``."""

from typing import Literal, TypeAlias, cast

ChannelType: TypeAlias = Literal[
    "BASIC",
    "STANDARD",
    "ADVANCED_SD",
    "ADVANCED_HD",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelType) -> str:
    return value


def deserialize_json(data: str) -> ChannelType:
    return cast(ChannelType, data)
