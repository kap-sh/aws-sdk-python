"""Generated from Smithy shape ``com.amazonaws.ec2#SecondaryInterfacePrivateIpAddressSpecificationListRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.secondary_interface_private_ip_address_specification_request

SecondaryInterfacePrivateIpAddressSpecificationListRequest: TypeAlias = list[
    "aws_sdk_ec2.types.secondary_interface_private_ip_address_specification_request.SecondaryInterfacePrivateIpAddressSpecificationRequest"
]
