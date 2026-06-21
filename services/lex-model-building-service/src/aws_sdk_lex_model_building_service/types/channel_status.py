"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#ChannelStatus``."""

from typing import Literal, TypeAlias, cast

ChannelStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "CREATED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelStatus) -> str:
    return value


def deserialize_json(data: str) -> ChannelStatus:
    return cast(ChannelStatus, data)
