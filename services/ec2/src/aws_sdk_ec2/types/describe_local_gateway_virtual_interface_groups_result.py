"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeLocalGatewayVirtualInterfaceGroupsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_virtual_interface_group_set
    import aws_sdk_ec2.types.string


class DescribeLocalGatewayVirtualInterfaceGroupsResult(TypedDict):
    local_gateway_virtual_interface_groups: NotRequired[
        "aws_sdk_ec2.types.local_gateway_virtual_interface_group_set.LocalGatewayVirtualInterfaceGroupSet"
    ]
    """<p>The virtual interface groups.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
