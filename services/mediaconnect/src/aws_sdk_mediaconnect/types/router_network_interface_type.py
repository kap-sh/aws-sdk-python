"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterNetworkInterfaceType``."""

from typing import Literal, TypeAlias, cast

RouterNetworkInterfaceType: TypeAlias = Literal[
    "PUBLIC",
    "VPC",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouterNetworkInterfaceType) -> str:
    return value


def deserialize_json(data: str) -> RouterNetworkInterfaceType:
    return cast(RouterNetworkInterfaceType, data)
