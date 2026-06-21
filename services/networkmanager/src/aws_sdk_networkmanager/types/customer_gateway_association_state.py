"""Generated from Smithy shape ``com.amazonaws.networkmanager#CustomerGatewayAssociationState``."""

from typing import Literal, TypeAlias, cast

CustomerGatewayAssociationState: TypeAlias = Literal[
    "PENDING",
    "AVAILABLE",
    "DELETING",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomerGatewayAssociationState) -> str:
    return value


def deserialize_json(data: str) -> CustomerGatewayAssociationState:
    return cast(CustomerGatewayAssociationState, data)
