"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelPrivacy``."""

from typing import Literal, TypeAlias, cast

ChannelPrivacy: TypeAlias = Literal[
    "PUBLIC",
    "PRIVATE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelPrivacy) -> str:
    return value


def deserialize_json(data: str) -> ChannelPrivacy:
    return cast(ChannelPrivacy, data)
