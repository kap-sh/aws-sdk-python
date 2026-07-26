"""Generated from Smithy shape ``com.amazonaws.medialive#ChannelAlertState``."""

from typing import Literal, TypeAlias, cast

"""The possible states of a channel alert. SET - The alert is actively happening. CLEARED - The alert is no longer happening."""
ChannelAlertState: TypeAlias = Literal[
    "SET",
    "CLEARED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelAlertState) -> str:
    return value


def deserialize_json(data: str) -> ChannelAlertState:
    return cast(ChannelAlertState, data)
