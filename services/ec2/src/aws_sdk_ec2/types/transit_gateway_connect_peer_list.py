"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayConnectPeerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_connect_peer

TransitGatewayConnectPeerList: TypeAlias = list[
    "aws_sdk_ec2.types.transit_gateway_connect_peer.TransitGatewayConnectPeer"
]
