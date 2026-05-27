"""Generated from Smithy shape ``com.amazonaws.ec2#Ipv6PrefixListResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipv6_prefix_specification_response

Ipv6PrefixListResponse: TypeAlias = list[
    "aws_sdk_ec2.types.ipv6_prefix_specification_response.Ipv6PrefixSpecificationResponse"
]
