"""Generated from Smithy shape ``com.amazonaws.medialive#ChannelState``."""

from typing import Literal, TypeAlias, cast

"""Placeholder documentation for ChannelState"""
ChannelState: TypeAlias = Literal[
    "CREATING",
    "CREATE_FAILED",
    "IDLE",
    "STARTING",
    "RUNNING",
    "RECOVERING",
    "STOPPING",
    "DELETING",
    "DELETED",
    "UPDATING",
    "UPDATE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelState) -> str:
    return value


def deserialize_json(data: str) -> ChannelState:
    return cast(ChannelState, data)
