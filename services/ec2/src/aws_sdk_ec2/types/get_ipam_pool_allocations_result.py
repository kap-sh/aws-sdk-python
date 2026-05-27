"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamPoolAllocationsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_pool_allocation_set
    import aws_sdk_ec2.types.next_token


class GetIpamPoolAllocationsResult(TypedDict):
    ipam_pool_allocations: NotRequired[
        "aws_sdk_ec2.types.ipam_pool_allocation_set.IpamPoolAllocationSet"
    ]
    """<p>The IPAM pool allocations you want information on.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
