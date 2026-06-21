"""Generated from Smithy shape ``com.amazonaws.networkmanager#GlobalNetworkState``."""

from typing import Literal, TypeAlias, cast

GlobalNetworkState: TypeAlias = Literal[
    "PENDING",
    "AVAILABLE",
    "DELETING",
    "UPDATING",
]


# --- restJson1 ser/de ---
def serialize_json(value: GlobalNetworkState) -> str:
    return value


def deserialize_json(data: str) -> GlobalNetworkState:
    return cast(GlobalNetworkState, data)
