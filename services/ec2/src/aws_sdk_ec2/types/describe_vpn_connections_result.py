"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpnConnectionsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpn_connection_list


class DescribeVpnConnectionsResult(TypedDict):
    vpn_connections: NotRequired[
        "aws_sdk_ec2.types.vpn_connection_list.VpnConnectionList"
    ]
    """<p>Information about one or more VPN connections.</p>"""
