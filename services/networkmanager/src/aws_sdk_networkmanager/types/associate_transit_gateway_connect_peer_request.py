"""Generated from Smithy shape ``com.amazonaws.networkmanager#AssociateTransitGatewayConnectPeerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_networkmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.device_id
    import aws_sdk_networkmanager.types.global_network_id
    import aws_sdk_networkmanager.types.link_id
    import aws_sdk_networkmanager.types.transit_gateway_connect_peer_arn


class AssociateTransitGatewayConnectPeerRequest(TypedDict, closed=True):
    global_network_id: "aws_sdk_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    transit_gateway_connect_peer_arn: "aws_sdk_networkmanager.types.transit_gateway_connect_peer_arn.TransitGatewayConnectPeerArn"
    """<p>The Amazon Resource Name (ARN) of the Connect peer.</p>"""
    device_id: "aws_sdk_networkmanager.types.device_id.DeviceId"
    """<p>The ID of the device.</p>"""
    link_id: NotRequired["aws_sdk_networkmanager.types.link_id.LinkId"]
    """<p>The ID of the link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateTransitGatewayConnectPeerRequest) -> dict:
    out: dict = {}
    out["TransitGatewayConnectPeerArn"] = value["transit_gateway_connect_peer_arn"]
    out["DeviceId"] = value["device_id"]
    if "link_id" in value:
        out["LinkId"] = value["link_id"]
    return out


def deserialize_json(data: dict) -> AssociateTransitGatewayConnectPeerRequest:
    out: AssociateTransitGatewayConnectPeerRequest = {}  # type: ignore[typeddict-item]
    if "TransitGatewayConnectPeerArn" in data:
        out["transit_gateway_connect_peer_arn"] = data["TransitGatewayConnectPeerArn"]
    else:
        raise DeserializationError(
            "AssociateTransitGatewayConnectPeerRequest.transit_gateway_connect_peer_arn required"
        )
    if "DeviceId" in data:
        out["device_id"] = data["DeviceId"]
    else:
        raise DeserializationError(
            "AssociateTransitGatewayConnectPeerRequest.device_id required"
        )
    if "LinkId" in data:
        out["link_id"] = data["LinkId"]
    return out
