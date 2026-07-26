"""Generated from Smithy shape ``com.amazonaws.networkmanager#TransitGatewayRegistrationState``."""

from typing import Literal, TypeAlias, cast

TransitGatewayRegistrationState: TypeAlias = Literal[
    "PENDING",
    "AVAILABLE",
    "DELETING",
    "DELETED",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: TransitGatewayRegistrationState) -> str:
    return value


def deserialize_json(data: str) -> TransitGatewayRegistrationState:
    return cast(TransitGatewayRegistrationState, data)
