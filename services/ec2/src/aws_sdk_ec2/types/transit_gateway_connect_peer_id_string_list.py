"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayConnectPeerIdStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_connect_peer_id

TransitGatewayConnectPeerIdStringList: TypeAlias = list[
    "aws_sdk_ec2.types.transit_gateway_connect_peer_id.TransitGatewayConnectPeerId"
]
