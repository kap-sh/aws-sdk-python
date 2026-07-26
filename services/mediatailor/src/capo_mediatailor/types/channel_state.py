"""Generated from Smithy shape ``com.amazonaws.mediatailor#ChannelState``."""

from typing import Literal, TypeAlias, cast

ChannelState: TypeAlias = Literal[
    "RUNNING",
    "STOPPED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelState) -> str:
    return value


def deserialize_json(data: str) -> ChannelState:
    return cast(ChannelState, data)
