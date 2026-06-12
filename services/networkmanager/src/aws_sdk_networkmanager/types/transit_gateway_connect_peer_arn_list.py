"""Generated from Smithy shape ``com.amazonaws.networkmanager#TransitGatewayConnectPeerArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.transit_gateway_connect_peer_arn

TransitGatewayConnectPeerArnList: TypeAlias = list[
    "aws_sdk_networkmanager.types.transit_gateway_connect_peer_arn.TransitGatewayConnectPeerArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: TransitGatewayConnectPeerArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> TransitGatewayConnectPeerArnList:
    return list(data)
