"""Generated from Smithy shape ``com.amazonaws.ec2#CreateLocalGatewayVirtualInterfaceGroupResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_virtual_interface_group


class CreateLocalGatewayVirtualInterfaceGroupResult(TypedDict):
    local_gateway_virtual_interface_group: NotRequired[
        "aws_sdk_ec2.types.local_gateway_virtual_interface_group.LocalGatewayVirtualInterfaceGroup"
    ]
    """<p>Information about the created local gateway virtual interface group.</p>"""
