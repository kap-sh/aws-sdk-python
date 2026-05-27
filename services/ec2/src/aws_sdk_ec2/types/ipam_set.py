"""Generated from Smithy shape ``com.amazonaws.ec2#IpamSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam

IpamSet: TypeAlias = list["aws_sdk_ec2.types.ipam.Ipam"]
