"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#ChannelRole``."""

from typing import Literal, TypeAlias, cast

ChannelRole: TypeAlias = Literal[
    "MASTER",
    "VIEWER",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelRole) -> str:
    return value


def deserialize_json(data: str) -> ChannelRole:
    return cast(ChannelRole, data)
