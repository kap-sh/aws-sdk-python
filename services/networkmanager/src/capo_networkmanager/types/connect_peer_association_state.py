"""Generated from Smithy shape ``com.amazonaws.networkmanager#ConnectPeerAssociationState``."""

from typing import Literal, TypeAlias, cast

ConnectPeerAssociationState: TypeAlias = Literal[
    "PENDING",
    "AVAILABLE",
    "DELETING",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectPeerAssociationState) -> str:
    return value


def deserialize_json(data: str) -> ConnectPeerAssociationState:
    return cast(ConnectPeerAssociationState, data)
