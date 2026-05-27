"""Generated from Smithy shape ``com.amazonaws.ec2#SupportedIpAddressTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.service_connectivity_type

SupportedIpAddressTypes: TypeAlias = list[
    "aws_sdk_ec2.types.service_connectivity_type.ServiceConnectivityType"
]
