"""Generated from Smithy shape ``com.amazonaws.ec2#DescribePublicIpv4PoolsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.public_ipv4_pool_set
    import aws_sdk_ec2.types.string


class DescribePublicIpv4PoolsResult(TypedDict):
    public_ipv4_pools: NotRequired[
        "aws_sdk_ec2.types.public_ipv4_pool_set.PublicIpv4PoolSet"
    ]
    """<p>Information about the address pools.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
