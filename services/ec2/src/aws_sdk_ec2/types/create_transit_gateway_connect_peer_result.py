"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayConnectPeerResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_connect_peer


class CreateTransitGatewayConnectPeerResult(TypedDict):
    transit_gateway_connect_peer: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_connect_peer.TransitGatewayConnectPeer"
    ]
    """<p>Information about the Connect peer.</p>"""
