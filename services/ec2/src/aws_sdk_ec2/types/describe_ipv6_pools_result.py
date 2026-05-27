"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIpv6PoolsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipv6_pool_set
    import aws_sdk_ec2.types.next_token


class DescribeIpv6PoolsResult(TypedDict):
    ipv6_pools: NotRequired["aws_sdk_ec2.types.ipv6_pool_set.Ipv6PoolSet"]
    """<p>Information about the IPv6 address pools.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
