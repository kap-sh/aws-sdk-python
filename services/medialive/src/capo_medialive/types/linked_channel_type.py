"""Generated from Smithy shape ``com.amazonaws.medialive#LinkedChannelType``."""

from typing import Literal, TypeAlias, cast

"""The values for the role for a linked channel."""
LinkedChannelType: TypeAlias = Literal[
    "FOLLOWING_CHANNEL",
    "PRIMARY_CHANNEL",
]


# --- restJson1 ser/de ---
def serialize_json(value: LinkedChannelType) -> str:
    return value


def deserialize_json(data: str) -> LinkedChannelType:
    return cast(LinkedChannelType, data)
