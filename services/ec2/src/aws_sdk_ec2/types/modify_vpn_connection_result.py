"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpnConnectionResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpn_connection


class ModifyVpnConnectionResult(TypedDict):
    vpn_connection: NotRequired["aws_sdk_ec2.types.vpn_connection.VpnConnection"]
    """<p>Information about the VPN connection.</p>"""
