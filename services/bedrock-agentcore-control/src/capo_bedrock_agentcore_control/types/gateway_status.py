"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GatewayStatus``."""

from typing import Literal, TypeAlias, cast

GatewayStatus: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "UPDATE_UNSUCCESSFUL",
    "DELETING",
    "READY",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: GatewayStatus) -> str:
    return value


def deserialize_json(data: str) -> GatewayStatus:
    return cast(GatewayStatus, data)
