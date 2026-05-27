"""Generated from Smithy shape ``com.amazonaws.ec2#CreateRouteServerPeerResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_server_peer


class CreateRouteServerPeerResult(TypedDict):
    route_server_peer: NotRequired[
        "aws_sdk_ec2.types.route_server_peer.RouteServerPeer"
    ]
    """<p>Information about the created route server peer.</p>"""
