"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteLocalGatewayRouteTableResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_route_table


class DeleteLocalGatewayRouteTableResult(TypedDict):
    local_gateway_route_table: NotRequired[
        "aws_sdk_ec2.types.local_gateway_route_table.LocalGatewayRouteTable"
    ]
    """<p>Information about the local gateway route table.</p>"""
