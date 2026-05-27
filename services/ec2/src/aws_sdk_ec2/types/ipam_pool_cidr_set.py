"""Generated from Smithy shape ``com.amazonaws.ec2#IpamPoolCidrSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_pool_cidr

IpamPoolCidrSet: TypeAlias = list["aws_sdk_ec2.types.ipam_pool_cidr.IpamPoolCidr"]
