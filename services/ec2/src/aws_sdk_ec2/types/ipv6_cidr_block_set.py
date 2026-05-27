"""Generated from Smithy shape ``com.amazonaws.ec2#Ipv6CidrBlockSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipv6_cidr_block

Ipv6CidrBlockSet: TypeAlias = list["aws_sdk_ec2.types.ipv6_cidr_block.Ipv6CidrBlock"]
