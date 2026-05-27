"""Generated from Smithy shape ``com.amazonaws.ec2#CreateNetworkInterfacePermissionRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.interface_permission_type
    import aws_sdk_ec2.types.network_interface_id
    import aws_sdk_ec2.types.string


class CreateNetworkInterfacePermissionRequest(TypedDict):
    network_interface_id: NotRequired[
        "aws_sdk_ec2.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The ID of the network interface.</p>"""
    aws_account_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID.</p>"""
    aws_service: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services service. Currently not supported.</p>"""
    permission: NotRequired[
        "aws_sdk_ec2.types.interface_permission_type.InterfacePermissionType"
    ]
    """<p>The type of permission to grant.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
