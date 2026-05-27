"""Generated from Smithy shape ``com.amazonaws.ec2#Ipv6PoolSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipv6_pool

Ipv6PoolSet: TypeAlias = list["aws_sdk_ec2.types.ipv6_pool.Ipv6Pool"]
