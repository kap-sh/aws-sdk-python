"""Generated from Smithy shape ``com.amazonaws.medialive#ChannelState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: ChannelState) -> str:
    return value


def deserialize_json(data: str) -> ChannelState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChannelState value: {data!r}")
    return cast(ChannelState, data)
