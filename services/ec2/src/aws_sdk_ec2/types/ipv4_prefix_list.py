"""Generated from Smithy shape ``com.amazonaws.ec2#Ipv4PrefixList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipv4_prefix_specification_request

Ipv4PrefixList: TypeAlias = list[
    "aws_sdk_ec2.types.ipv4_prefix_specification_request.Ipv4PrefixSpecificationRequest"
]
