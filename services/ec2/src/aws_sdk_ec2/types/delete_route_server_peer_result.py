"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteRouteServerPeerResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_server_peer


class DeleteRouteServerPeerResult(TypedDict):
    route_server_peer: NotRequired[
        "aws_sdk_ec2.types.route_server_peer.RouteServerPeer"
    ]
    """<p>Information about the deleted route server peer.</p>"""
