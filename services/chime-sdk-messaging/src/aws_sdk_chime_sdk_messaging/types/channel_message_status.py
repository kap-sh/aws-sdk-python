"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelMessageStatus``."""

from typing import Literal, TypeAlias, cast

ChannelMessageStatus: TypeAlias = Literal[
    "SENT",
    "PENDING",
    "FAILED",
    "DENIED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelMessageStatus) -> str:
    return value


def deserialize_json(data: str) -> ChannelMessageStatus:
    return cast(ChannelMessageStatus, data)
