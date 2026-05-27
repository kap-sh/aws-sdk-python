"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTransitGatewayConnectPeerResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_connect_peer


class DeleteTransitGatewayConnectPeerResult(TypedDict):
    transit_gateway_connect_peer: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_connect_peer.TransitGatewayConnectPeer"
    ]
    """<p>Information about the deleted Connect peer.</p>"""
