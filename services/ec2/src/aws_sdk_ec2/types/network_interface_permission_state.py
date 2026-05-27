"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInterfacePermissionState``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_interface_permission_state_code
    import aws_sdk_ec2.types.string


class NetworkInterfacePermissionState(TypedDict):
    state: NotRequired[
        "aws_sdk_ec2.types.network_interface_permission_state_code.NetworkInterfacePermissionStateCode"
    ]
    """<p>The state of the permission.</p>"""
    status_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A status message, if applicable.</p>"""
