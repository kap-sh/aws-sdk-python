"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceIpv4PrefixList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_ipv4_prefix

InstanceIpv4PrefixList: TypeAlias = list[
    "aws_sdk_ec2.types.instance_ipv4_prefix.InstanceIpv4Prefix"
]
