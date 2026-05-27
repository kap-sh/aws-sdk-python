"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeLocalGatewayRouteTablesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_route_table_set
    import aws_sdk_ec2.types.string


class DescribeLocalGatewayRouteTablesResult(TypedDict):
    local_gateway_route_tables: NotRequired[
        "aws_sdk_ec2.types.local_gateway_route_table_set.LocalGatewayRouteTableSet"
    ]
    """<p>Information about the local gateway route tables.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
