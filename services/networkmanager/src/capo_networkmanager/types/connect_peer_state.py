"""Generated from Smithy shape ``com.amazonaws.networkmanager#ConnectPeerState``."""

from typing import Literal, TypeAlias, cast

ConnectPeerState: TypeAlias = Literal[
    "CREATING",
    "FAILED",
    "AVAILABLE",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectPeerState) -> str:
    return value


def deserialize_json(data: str) -> ConnectPeerState:
    return cast(ConnectPeerState, data)
