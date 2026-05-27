"""Generated from Smithy shape ``com.amazonaws.ec2#PublicIpv4PoolIdStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipv4_pool_ec2_id

PublicIpv4PoolIdStringList: TypeAlias = list[
    "aws_sdk_ec2.types.ipv4_pool_ec2_id.Ipv4PoolEc2Id"
]
