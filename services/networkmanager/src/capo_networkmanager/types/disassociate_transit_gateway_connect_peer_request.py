"""Generated from Smithy shape ``com.amazonaws.networkmanager#DisassociateTransitGatewayConnectPeerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.global_network_id
    import capo_networkmanager.types.transit_gateway_connect_peer_arn


class DisassociateTransitGatewayConnectPeerRequest(TypedDict, closed=True):
    global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    transit_gateway_connect_peer_arn: "capo_networkmanager.types.transit_gateway_connect_peer_arn.TransitGatewayConnectPeerArn"
    """<p>The Amazon Resource Name (ARN) of the transit gateway Connect peer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateTransitGatewayConnectPeerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateTransitGatewayConnectPeerRequest:
    out: DisassociateTransitGatewayConnectPeerRequest = {}  # type: ignore[typeddict-item]
    return out
