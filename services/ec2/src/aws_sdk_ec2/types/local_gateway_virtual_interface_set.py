"""Generated from Smithy shape ``com.amazonaws.ec2#LocalGatewayVirtualInterfaceSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_virtual_interface

LocalGatewayVirtualInterfaceSet: TypeAlias = list[
    "aws_sdk_ec2.types.local_gateway_virtual_interface.LocalGatewayVirtualInterface"
]
