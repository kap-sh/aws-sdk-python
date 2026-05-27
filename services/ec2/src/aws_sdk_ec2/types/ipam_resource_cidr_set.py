"""Generated from Smithy shape ``com.amazonaws.ec2#IpamResourceCidrSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_resource_cidr

IpamResourceCidrSet: TypeAlias = list[
    "aws_sdk_ec2.types.ipam_resource_cidr.IpamResourceCidr"
]
