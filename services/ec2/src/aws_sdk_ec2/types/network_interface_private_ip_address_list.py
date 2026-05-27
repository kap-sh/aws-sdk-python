"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInterfacePrivateIpAddressList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_interface_private_ip_address

NetworkInterfacePrivateIpAddressList: TypeAlias = list[
    "aws_sdk_ec2.types.network_interface_private_ip_address.NetworkInterfacePrivateIpAddress"
]
