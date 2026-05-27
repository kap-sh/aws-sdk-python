"""Generated from Smithy shape ``com.amazonaws.ec2#SecondaryInterfaceIpv4AddressList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.secondary_interface_ipv4_address

SecondaryInterfaceIpv4AddressList: TypeAlias = list[
    "aws_sdk_ec2.types.secondary_interface_ipv4_address.SecondaryInterfaceIpv4Address"
]
