"""Generated from Smithy shape ``com.amazonaws.ec2#ClientVpnConnectionStatus``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_vpn_connection_status_code
    import aws_sdk_ec2.types.string


class ClientVpnConnectionStatus(TypedDict):
    code: NotRequired[
        "aws_sdk_ec2.types.client_vpn_connection_status_code.ClientVpnConnectionStatusCode"
    ]
    """<p>The state of the client connection.</p>"""
    message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A message about the status of the client connection, if applicable.</p>"""
