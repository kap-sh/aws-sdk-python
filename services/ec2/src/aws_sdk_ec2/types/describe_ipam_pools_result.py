"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIpamPoolsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_pool_set
    import aws_sdk_ec2.types.next_token


class DescribeIpamPoolsResult(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    ipam_pools: NotRequired["aws_sdk_ec2.types.ipam_pool_set.IpamPoolSet"]
    """<p>Information about the IPAM pools.</p>"""
