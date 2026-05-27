"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTransitGatewayRouteTableResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_route_table


class DeleteTransitGatewayRouteTableResult(TypedDict):
    transit_gateway_route_table: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_route_table.TransitGatewayRouteTable"
    ]
    """<p>Information about the deleted transit gateway route table.</p>"""
