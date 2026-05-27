"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeLocalGatewayRouteTableVpcAssociationsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_route_table_vpc_association_set
    import aws_sdk_ec2.types.string


class DescribeLocalGatewayRouteTableVpcAssociationsResult(TypedDict):
    local_gateway_route_table_vpc_associations: NotRequired[
        "aws_sdk_ec2.types.local_gateway_route_table_vpc_association_set.LocalGatewayRouteTableVpcAssociationSet"
    ]
    """<p>Information about the associations.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
