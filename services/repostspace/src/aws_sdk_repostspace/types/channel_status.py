"""Generated from Smithy shape ``com.amazonaws.repostspace#ChannelStatus``."""

from typing import Literal, TypeAlias, cast

ChannelStatus: TypeAlias = Literal[
    "CREATED",
    "CREATING",
    "CREATE_FAILED",
    "DELETED",
    "DELETING",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelStatus) -> str:
    return value


def deserialize_json(data: str) -> ChannelStatus:
    return cast(ChannelStatus, data)
