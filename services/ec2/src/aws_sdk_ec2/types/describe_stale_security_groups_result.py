"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeStaleSecurityGroupsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.stale_security_group_set
    import aws_sdk_ec2.types.string


class DescribeStaleSecurityGroupsResult(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    stale_security_group_set: NotRequired[
        "aws_sdk_ec2.types.stale_security_group_set.StaleSecurityGroupSet"
    ]
    """<p>Information about the stale security groups.</p>"""
