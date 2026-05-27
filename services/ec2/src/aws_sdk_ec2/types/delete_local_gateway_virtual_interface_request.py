"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteLocalGatewayVirtualInterfaceRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.local_gateway_virtual_interface_id


class DeleteLocalGatewayVirtualInterfaceRequest(TypedDict):
    local_gateway_virtual_interface_id: NotRequired[
        "aws_sdk_ec2.types.local_gateway_virtual_interface_id.LocalGatewayVirtualInterfaceId"
    ]
    """<p>The ID of the local virtual interface to delete.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
