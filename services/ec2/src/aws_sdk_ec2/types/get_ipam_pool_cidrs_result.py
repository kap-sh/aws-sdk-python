"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamPoolCidrsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_pool_cidr_set
    import aws_sdk_ec2.types.next_token


class GetIpamPoolCidrsResult(TypedDict):
    ipam_pool_cidrs: NotRequired["aws_sdk_ec2.types.ipam_pool_cidr_set.IpamPoolCidrSet"]
    """<p>Information about the CIDRs provisioned to an IPAM pool.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
