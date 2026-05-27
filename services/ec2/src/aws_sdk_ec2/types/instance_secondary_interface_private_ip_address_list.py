"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceSecondaryInterfacePrivateIpAddressList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_secondary_interface_private_ip_address

InstanceSecondaryInterfacePrivateIpAddressList: TypeAlias = list[
    "aws_sdk_ec2.types.instance_secondary_interface_private_ip_address.InstanceSecondaryInterfacePrivateIpAddress"
]
