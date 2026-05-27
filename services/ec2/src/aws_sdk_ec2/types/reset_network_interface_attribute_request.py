"""Generated from Smithy shape ``com.amazonaws.ec2#ResetNetworkInterfaceAttributeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.network_interface_id
    import aws_sdk_ec2.types.string


class ResetNetworkInterfaceAttributeRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    network_interface_id: NotRequired[
        "aws_sdk_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the network interface.</p>"""
    source_dest_check: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The source/destination checking attribute. Resets the value to <code>true</code>.</p>"""
