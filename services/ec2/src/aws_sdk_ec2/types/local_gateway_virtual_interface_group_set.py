"""Generated from Smithy shape ``com.amazonaws.ec2#LocalGatewayVirtualInterfaceGroupSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_virtual_interface_group

LocalGatewayVirtualInterfaceGroupSet: TypeAlias = list[
    "aws_sdk_ec2.types.local_gateway_virtual_interface_group.LocalGatewayVirtualInterfaceGroup"
]
