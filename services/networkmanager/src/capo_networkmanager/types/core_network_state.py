"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkState``."""

from typing import Literal, TypeAlias, cast

CoreNetworkState: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "AVAILABLE",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkState) -> str:
    return value


def deserialize_json(data: str) -> CoreNetworkState:
    return cast(CoreNetworkState, data)
