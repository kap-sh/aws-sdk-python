"""Generated from Smithy shape ``com.amazonaws.networkmanager#DisassociateTransitGatewayConnectPeerRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.global_network_id
    import aws_sdk_networkmanager.types.transit_gateway_connect_peer_arn


class DisassociateTransitGatewayConnectPeerRequest(TypedDict):
    global_network_id: "aws_sdk_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    transit_gateway_connect_peer_arn: "aws_sdk_networkmanager.types.transit_gateway_connect_peer_arn.TransitGatewayConnectPeerArn"
    """<p>The Amazon Resource Name (ARN) of the transit gateway Connect peer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateTransitGatewayConnectPeerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateTransitGatewayConnectPeerRequest:
    out: DisassociateTransitGatewayConnectPeerRequest = {}  # type: ignore[typeddict-item]
    return out
