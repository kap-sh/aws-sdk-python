"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerPeersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_server_peer

RouteServerPeersList: TypeAlias = list[
    "aws_sdk_ec2.types.route_server_peer.RouteServerPeer"
]
