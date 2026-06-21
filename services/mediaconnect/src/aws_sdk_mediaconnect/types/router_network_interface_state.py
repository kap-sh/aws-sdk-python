"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterNetworkInterfaceState``."""

from typing import Literal, TypeAlias, cast

RouterNetworkInterfaceState: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
    "ERROR",
    "RECOVERING",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouterNetworkInterfaceState) -> str:
    return value


def deserialize_json(data: str) -> RouterNetworkInterfaceState:
    return cast(RouterNetworkInterfaceState, data)
