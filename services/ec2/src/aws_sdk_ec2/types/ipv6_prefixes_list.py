"""Generated from Smithy shape ``com.amazonaws.ec2#Ipv6PrefixesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipv6_prefix_specification

Ipv6PrefixesList: TypeAlias = list[
    "aws_sdk_ec2.types.ipv6_prefix_specification.Ipv6PrefixSpecification"
]
