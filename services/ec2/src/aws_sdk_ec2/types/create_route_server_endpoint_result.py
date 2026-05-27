"""Generated from Smithy shape ``com.amazonaws.ec2#CreateRouteServerEndpointResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_server_endpoint


class CreateRouteServerEndpointResult(TypedDict):
    route_server_endpoint: NotRequired[
        "aws_sdk_ec2.types.route_server_endpoint.RouteServerEndpoint"
    ]
    """<p>Information about the created route server endpoint.</p>"""
