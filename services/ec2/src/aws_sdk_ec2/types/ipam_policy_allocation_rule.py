"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPolicyAllocationRule``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_pool_id


class IpamPolicyAllocationRule(TypedDict):
    source_ipam_pool_id: NotRequired["aws_sdk_ec2.types.ipam_pool_id.IpamPoolId"]
    """<p>The ID of the source IPAM pool for the allocation rule.</p> <p>An IPAM pool is a collection of IP addresses in IPAM that can be allocated to Amazon Web Services resources.</p>"""
