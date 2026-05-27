"""Generated from Smithy shape ``com.amazonaws.ec2#GetActiveVpnTunnelStatusResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.active_vpn_tunnel_status


class GetActiveVpnTunnelStatusResult(TypedDict):
    active_vpn_tunnel_status: NotRequired[
        "aws_sdk_ec2.types.active_vpn_tunnel_status.ActiveVpnTunnelStatus"
    ]
    """<p>Information about the current security configuration of the VPN tunnel.</p>"""
