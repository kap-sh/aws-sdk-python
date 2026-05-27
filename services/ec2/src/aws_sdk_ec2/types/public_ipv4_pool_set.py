"""Generated from Smithy shape ``com.amazonaws.ec2#PublicIpv4PoolSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.public_ipv4_pool

PublicIpv4PoolSet: TypeAlias = list["aws_sdk_ec2.types.public_ipv4_pool.PublicIpv4Pool"]
