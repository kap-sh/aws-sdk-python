"""Generated from Smithy shape ``com.amazonaws.ec2#GetSecurityGroupsForVpcResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.security_group_for_vpc_list
    import aws_sdk_ec2.types.string


class GetSecurityGroupsForVpcResult(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    security_group_for_vpcs: NotRequired[
        "aws_sdk_ec2.types.security_group_for_vpc_list.SecurityGroupForVpcList"
    ]
    """<p>The security group that can be used by interfaces in the VPC.</p>"""
