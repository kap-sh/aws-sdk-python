"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_route_table_virtual_interface_group_association_set
    import aws_sdk_ec2.types.string


class DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResult(TypedDict):
    local_gateway_route_table_virtual_interface_group_associations: NotRequired[
        "aws_sdk_ec2.types.local_gateway_route_table_virtual_interface_group_association_set.LocalGatewayRouteTableVirtualInterfaceGroupAssociationSet"
    ]
    """<p>Information about the associations.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
