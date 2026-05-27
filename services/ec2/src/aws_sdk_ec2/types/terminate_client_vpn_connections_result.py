"""Generated from Smithy shape ``com.amazonaws.ec2#TerminateClientVpnConnectionsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.terminate_connection_status_set


class TerminateClientVpnConnectionsResult(TypedDict):
    client_vpn_endpoint_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Client VPN endpoint.</p>"""
    username: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The user who established the terminated client connections.</p>"""
    connection_statuses: NotRequired[
        "aws_sdk_ec2.types.terminate_connection_status_set.TerminateConnectionStatusSet"
    ]
    """<p>The current state of the client connections.</p>"""
