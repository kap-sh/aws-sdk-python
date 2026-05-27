"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayRouteTableResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_route_table


class CreateTransitGatewayRouteTableResult(TypedDict):
    transit_gateway_route_table: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_route_table.TransitGatewayRouteTable"
    ]
    """<p>Information about the transit gateway route table.</p>"""
