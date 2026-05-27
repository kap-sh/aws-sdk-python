"""Generated from Smithy shape ``com.amazonaws.ec2#CreateNetworkInterfacePermissionResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_interface_permission


class CreateNetworkInterfacePermissionResult(TypedDict):
    interface_permission: NotRequired[
        "aws_sdk_ec2.types.network_interface_permission.NetworkInterfacePermission"
    ]
    """<p>Information about the permission for the network interface.</p>"""
