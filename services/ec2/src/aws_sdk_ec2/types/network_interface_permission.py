"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInterfacePermission``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.interface_permission_type
    import aws_sdk_ec2.types.network_interface_permission_state
    import aws_sdk_ec2.types.string


class NetworkInterfacePermission(TypedDict):
    network_interface_permission_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the network interface permission.</p>"""
    network_interface_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the network interface.</p>"""
    aws_account_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services account ID.</p>"""
    aws_service: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Web Services service.</p>"""
    permission: NotRequired[
        "aws_sdk_ec2.types.interface_permission_type.InterfacePermissionType"
    ]
    """<p>The type of permission.</p>"""
    permission_state: NotRequired[
        "aws_sdk_ec2.types.network_interface_permission_state.NetworkInterfacePermissionState"
    ]
    """<p>Information about the state of the permission.</p>"""
