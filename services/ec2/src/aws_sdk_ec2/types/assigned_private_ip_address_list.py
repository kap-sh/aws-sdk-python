"""Generated from Smithy shape ``com.amazonaws.ec2#AssignedPrivateIpAddressList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.assigned_private_ip_address

AssignedPrivateIpAddressList: TypeAlias = list[
    "aws_sdk_ec2.types.assigned_private_ip_address.AssignedPrivateIpAddress"
]
