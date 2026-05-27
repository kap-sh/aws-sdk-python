"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInterfaceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_interface

NetworkInterfaceList: TypeAlias = list[
    "aws_sdk_ec2.types.network_interface.NetworkInterface"
]
