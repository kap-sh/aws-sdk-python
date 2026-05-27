"""Generated from Smithy shape ``com.amazonaws.ec2#PublicIpv4PoolRangeSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.public_ipv4_pool_range

PublicIpv4PoolRangeSet: TypeAlias = list[
    "aws_sdk_ec2.types.public_ipv4_pool_range.PublicIpv4PoolRange"
]
