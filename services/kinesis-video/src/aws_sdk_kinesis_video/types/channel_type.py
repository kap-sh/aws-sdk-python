"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#ChannelType``."""

from typing import Literal, TypeAlias, cast

ChannelType: TypeAlias = Literal[
    "SINGLE_MASTER",
    "FULL_MESH",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelType) -> str:
    return value


def deserialize_json(data: str) -> ChannelType:
    return cast(ChannelType, data)
