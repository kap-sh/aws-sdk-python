"""Generated from Smithy shape ``com.amazonaws.ec2#GetTransitGatewayRouteTablePropagationsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_route_table_propagation_list


class GetTransitGatewayRouteTablePropagationsResult(TypedDict):
    transit_gateway_route_table_propagations: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_route_table_propagation_list.TransitGatewayRouteTablePropagationList"
    ]
    """<p>Information about the route table propagations.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
