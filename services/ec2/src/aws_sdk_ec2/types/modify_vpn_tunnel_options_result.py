"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpnTunnelOptionsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpn_connection


class ModifyVpnTunnelOptionsResult(TypedDict):
    vpn_connection: NotRequired["aws_sdk_ec2.types.vpn_connection.VpnConnection"]
    """<p>Information about the VPN connection.</p>"""
