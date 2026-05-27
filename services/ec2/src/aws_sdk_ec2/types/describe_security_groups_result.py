"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSecurityGroupsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.security_group_list
    import aws_sdk_ec2.types.string


class DescribeSecurityGroupsResult(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    security_groups: NotRequired[
        "aws_sdk_ec2.types.security_group_list.SecurityGroupList"
    ]
    """<p>Information about the security groups.</p>"""
