"""Generated from Smithy shape ``com.amazonaws.ec2#RouteServerPeerIdsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_server_peer_id

RouteServerPeerIdsList: TypeAlias = list[
    "aws_sdk_ec2.types.route_server_peer_id.RouteServerPeerId"
]
