"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVerifiedAccessGroupsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.next_token
    import aws_sdk_ec2.types.verified_access_group_list


class DescribeVerifiedAccessGroupsResult(TypedDict):
    verified_access_groups: NotRequired[
        "aws_sdk_ec2.types.verified_access_group_list.VerifiedAccessGroupList"
    ]
    """<p>Details about the Verified Access groups.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
