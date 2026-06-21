"""Generated from Smithy shape ``com.amazonaws.mediaconnect#GatewayState``."""

from typing import Literal, TypeAlias, cast

GatewayState: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "ERROR",
    "DELETING",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: GatewayState) -> str:
    return value


def deserialize_json(data: str) -> GatewayState:
    return cast(GatewayState, data)
