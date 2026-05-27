"""Generated from Smithy shape ``com.amazonaws.ec2#PrivateIpAddressSpecificationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.private_ip_address_specification

PrivateIpAddressSpecificationList: TypeAlias = list[
    "aws_sdk_ec2.types.private_ip_address_specification.PrivateIpAddressSpecification"
]
