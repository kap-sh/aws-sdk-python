"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPoolSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_pool

IpamPoolSet: TypeAlias = list["aws_sdk_ec2.types.ipam_pool.IpamPool"]
