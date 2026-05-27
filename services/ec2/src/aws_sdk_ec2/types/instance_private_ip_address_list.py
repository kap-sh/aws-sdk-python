"""Generated from Smithy shape ``com.amazonaws.ec2#InstancePrivateIpAddressList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_private_ip_address

InstancePrivateIpAddressList: TypeAlias = list[
    "aws_sdk_ec2.types.instance_private_ip_address.InstancePrivateIpAddress"
]
