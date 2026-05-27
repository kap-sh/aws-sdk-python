"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteRouteServerEndpointResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_server_endpoint


class DeleteRouteServerEndpointResult(TypedDict):
    route_server_endpoint: NotRequired[
        "aws_sdk_ec2.types.route_server_endpoint.RouteServerEndpoint"
    ]
    """<p>Information about the deleted route server endpoint.</p>"""
