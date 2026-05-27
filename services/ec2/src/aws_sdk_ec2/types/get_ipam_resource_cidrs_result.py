"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamResourceCidrsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_resource_cidr_set
    import aws_sdk_ec2.types.next_token


class GetIpamResourceCidrsResult(TypedDict):
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""
    ipam_resource_cidrs: NotRequired[
        "aws_sdk_ec2.types.ipam_resource_cidr_set.IpamResourceCidrSet"
    ]
    """<p>The resource CIDRs.</p>"""
