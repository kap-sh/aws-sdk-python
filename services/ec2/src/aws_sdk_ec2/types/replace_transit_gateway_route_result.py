"""Generated from Smithy shape ``com.amazonaws.ec2#ReplaceTransitGatewayRouteResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_route


class ReplaceTransitGatewayRouteResult(TypedDict):
    route: NotRequired["aws_sdk_ec2.types.transit_gateway_route.TransitGatewayRoute"]
    """<p>Information about the modified route.</p>"""
