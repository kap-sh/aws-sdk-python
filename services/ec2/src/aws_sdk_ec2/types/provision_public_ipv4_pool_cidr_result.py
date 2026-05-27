"""Generated from Smithy shape ``com.amazonaws.ec2#ProvisionPublicIpv4PoolCidrResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipv4_pool_ec2_id
    import aws_sdk_ec2.types.public_ipv4_pool_range


class ProvisionPublicIpv4PoolCidrResult(TypedDict):
    pool_id: NotRequired["aws_sdk_ec2.types.ipv4_pool_ec2_id.Ipv4PoolEc2Id"]
    """<p>The ID of the pool that you want to provision the CIDR to.</p>"""
    pool_address_range: NotRequired[
        "aws_sdk_ec2.types.public_ipv4_pool_range.PublicIpv4PoolRange"
    ]
    """<p>Information about the address range of the public IPv4 pool.</p>"""
