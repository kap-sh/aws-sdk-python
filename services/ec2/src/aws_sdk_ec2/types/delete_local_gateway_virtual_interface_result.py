"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteLocalGatewayVirtualInterfaceResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_virtual_interface


class DeleteLocalGatewayVirtualInterfaceResult(TypedDict):
    local_gateway_virtual_interface: NotRequired[
        "aws_sdk_ec2.types.local_gateway_virtual_interface.LocalGatewayVirtualInterface"
    ]
    """<p>Information about the deleted local gateway virtual interface.</p>"""
