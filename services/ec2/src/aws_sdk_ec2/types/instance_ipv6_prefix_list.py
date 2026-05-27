"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceIpv6PrefixList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_ipv6_prefix

InstanceIpv6PrefixList: TypeAlias = list[
    "aws_sdk_ec2.types.instance_ipv6_prefix.InstanceIpv6Prefix"
]
