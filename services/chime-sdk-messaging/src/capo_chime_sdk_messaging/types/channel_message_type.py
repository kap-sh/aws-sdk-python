"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelMessageType``."""

from typing import Literal, TypeAlias, cast

ChannelMessageType: TypeAlias = Literal[
    "STANDARD",
    "CONTROL",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelMessageType) -> str:
    return value


def deserialize_json(data: str) -> ChannelMessageType:
    return cast(ChannelMessageType, data)
