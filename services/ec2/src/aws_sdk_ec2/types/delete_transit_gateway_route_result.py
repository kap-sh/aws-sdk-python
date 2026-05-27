"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTransitGatewayRouteResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_route


class DeleteTransitGatewayRouteResult(TypedDict):
    route: NotRequired["aws_sdk_ec2.types.transit_gateway_route.TransitGatewayRoute"]
    """<p>Information about the route.</p>"""
