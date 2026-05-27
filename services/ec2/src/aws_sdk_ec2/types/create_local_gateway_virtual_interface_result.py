"""Generated from Smithy shape ``com.amazonaws.ec2#CreateLocalGatewayVirtualInterfaceResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_virtual_interface


class CreateLocalGatewayVirtualInterfaceResult(TypedDict):
    local_gateway_virtual_interface: NotRequired[
        "aws_sdk_ec2.types.local_gateway_virtual_interface.LocalGatewayVirtualInterface"
    ]
    """<p>Information about the local gateway virtual interface.</p>"""
