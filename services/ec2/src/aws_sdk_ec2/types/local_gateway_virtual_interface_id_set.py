"""Generated from Smithy shape ``com.amazonaws.ec2#LocalGatewayVirtualInterfaceIdSet``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_virtual_interface_id

LocalGatewayVirtualInterfaceIdSet: TypeAlias = list[
    "aws_sdk_ec2.types.local_gateway_virtual_interface_id.LocalGatewayVirtualInterfaceId"
]
