"""Generated from Smithy shape ``com.amazonaws.ec2#DeprovisionPublicIpv4PoolCidrResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.deprovisioned_address_set
    import aws_sdk_ec2.types.ipv4_pool_ec2_id


class DeprovisionPublicIpv4PoolCidrResult(TypedDict):
    pool_id: NotRequired["aws_sdk_ec2.types.ipv4_pool_ec2_id.Ipv4PoolEc2Id"]
    """<p>The ID of the pool that you deprovisioned the CIDR from.</p>"""
    deprovisioned_addresses: NotRequired[
        "aws_sdk_ec2.types.deprovisioned_address_set.DeprovisionedAddressSet"
    ]
    """<p>The deprovisioned CIDRs.</p>"""
