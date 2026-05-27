"""Generated from Smithy shape ``com.amazonaws.ec2#PrivateDnsDetailsSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.private_dns_details

PrivateDnsDetailsSet: TypeAlias = list[
    "aws_sdk_ec2.types.private_dns_details.PrivateDnsDetails"
]
