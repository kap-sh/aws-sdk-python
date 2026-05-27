"""Generated from Smithy shape ``com.amazonaws.ec2#TerminateConnectionStatus``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_vpn_connection_status
    import aws_sdk_ec2.types.string


class TerminateConnectionStatus(TypedDict):
    connection_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the client connection.</p>"""
    previous_status: NotRequired[
        "aws_sdk_ec2.types.client_vpn_connection_status.ClientVpnConnectionStatus"
    ]
    """<p>The state of the client connection.</p>"""
    current_status: NotRequired[
        "aws_sdk_ec2.types.client_vpn_connection_status.ClientVpnConnectionStatus"
    ]
    """<p>A message about the status of the client connection, if applicable.</p>"""
