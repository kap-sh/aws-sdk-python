"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelMembershipType``."""

from typing import Literal, TypeAlias, cast

ChannelMembershipType: TypeAlias = Literal[
    "DEFAULT",
    "HIDDEN",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelMembershipType) -> str:
    return value


def deserialize_json(data: str) -> ChannelMembershipType:
    return cast(ChannelMembershipType, data)
