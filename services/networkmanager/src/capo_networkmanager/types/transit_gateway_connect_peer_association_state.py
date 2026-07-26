"""Generated from Smithy shape ``com.amazonaws.networkmanager#TransitGatewayConnectPeerAssociationState``."""

from typing import Literal, TypeAlias, cast

TransitGatewayConnectPeerAssociationState: TypeAlias = Literal[
    "PENDING",
    "AVAILABLE",
    "DELETING",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: TransitGatewayConnectPeerAssociationState) -> str:
    return value


def deserialize_json(data: str) -> TransitGatewayConnectPeerAssociationState:
    return cast(TransitGatewayConnectPeerAssociationState, data)
