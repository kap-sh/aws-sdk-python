"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpnConnectionOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpn_connection_id
    import aws_sdk_ec2.types.vpn_tunnel_bandwidth


class ModifyVpnConnectionOptionsRequest(TypedDict):
    vpn_connection_id: NotRequired[
        "aws_sdk_ec2.types.vpn_connection_id.VpnConnectionId"
    ]
    """<p>The ID of the Site-to-Site VPN connection. </p>"""
    local_ipv4_network_cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 CIDR on the customer gateway (on-premises) side of the VPN connection.</p> <p>Default: <code>0.0.0.0/0</code> </p>"""
    remote_ipv4_network_cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 CIDR on the Amazon Web Services side of the VPN connection.</p> <p>Default: <code>0.0.0.0/0</code> </p>"""
    local_ipv6_network_cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv6 CIDR on the customer gateway (on-premises) side of the VPN connection.</p> <p>Default: <code>::/0</code> </p>"""
    remote_ipv6_network_cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv6 CIDR on the Amazon Web Services side of the VPN connection.</p> <p>Default: <code>::/0</code> </p>"""
    tunnel_bandwidth: NotRequired[
        "aws_sdk_ec2.types.vpn_tunnel_bandwidth.VpnTunnelBandwidth"
    ]
    """<p>The desired bandwidth specification for the VPN connection. <code>standard</code> supports up to 1.25 Gbps per tunnel, while <code>large</code> supports up to 5 Gbps per tunnel. Large bandwidth is only available for VPN connections attached to a transit gateway or to Cloud WAN. The default value is <code>standard</code>.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
