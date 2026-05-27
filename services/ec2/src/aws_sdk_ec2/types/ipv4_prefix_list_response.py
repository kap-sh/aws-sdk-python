"""Generated from Smithy shape ``com.amazonaws.ec2#Ipv4PrefixListResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipv4_prefix_specification_response

Ipv4PrefixListResponse: TypeAlias = list[
    "aws_sdk_ec2.types.ipv4_prefix_specification_response.Ipv4PrefixSpecificationResponse"
]
