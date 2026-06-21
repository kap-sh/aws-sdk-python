"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelMode``."""

from typing import Literal, TypeAlias, cast

ChannelMode: TypeAlias = Literal[
    "UNRESTRICTED",
    "RESTRICTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelMode) -> str:
    return value


def deserialize_json(data: str) -> ChannelMode:
    return cast(ChannelMode, data)
