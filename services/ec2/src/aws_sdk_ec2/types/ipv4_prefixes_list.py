"""Generated from Smithy shape ``com.amazonaws.ec2#Ipv4PrefixesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipv4_prefix_specification

Ipv4PrefixesList: TypeAlias = list[
    "aws_sdk_ec2.types.ipv4_prefix_specification.Ipv4PrefixSpecification"
]
