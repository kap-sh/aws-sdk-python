"""Generated from Smithy shape ``com.amazonaws.ec2#CreateLocalGatewayRouteResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_route


class CreateLocalGatewayRouteResult(TypedDict):
    route: NotRequired["aws_sdk_ec2.types.local_gateway_route.LocalGatewayRoute"]
    """<p>Information about the route.</p>"""
