"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInterfaceIpv6AddressesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_interface_ipv6_address

NetworkInterfaceIpv6AddressesList: TypeAlias = list[
    "aws_sdk_ec2.types.network_interface_ipv6_address.NetworkInterfaceIpv6Address"
]
