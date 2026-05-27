"""Generated from Smithy shape ``com.amazonaws.ec2#CreateRouteServerResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_server


class CreateRouteServerResult(TypedDict):
    route_server: NotRequired["aws_sdk_ec2.types.route_server.RouteServer"]
    """<p>Information about the created route server.</p>"""
