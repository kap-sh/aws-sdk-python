"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceSecondaryInterfacePrivateIpAddressListRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_secondary_interface_private_ip_address_request

InstanceSecondaryInterfacePrivateIpAddressListRequest: TypeAlias = list[
    "aws_sdk_ec2.types.instance_secondary_interface_private_ip_address_request.InstanceSecondaryInterfacePrivateIpAddressRequest"
]
