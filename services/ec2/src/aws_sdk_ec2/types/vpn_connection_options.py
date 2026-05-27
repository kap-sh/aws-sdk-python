"""Generated from Smithy shape ``com.amazonaws.ec2#VpnConnectionOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tunnel_inside_ip_version
    import aws_sdk_ec2.types.tunnel_options_list
    import aws_sdk_ec2.types.vpn_tunnel_bandwidth


class VpnConnectionOptions(TypedDict):
    enable_acceleration: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether acceleration is enabled for the VPN connection.</p>"""
    static_routes_only: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the VPN connection uses static routes only. Static routes must be used for devices that don't support BGP.</p>"""
    local_ipv4_network_cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 CIDR on the customer gateway (on-premises) side of the VPN connection.</p>"""
    remote_ipv4_network_cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 CIDR on the Amazon Web Services side of the VPN connection.</p>"""
    local_ipv6_network_cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv6 CIDR on the customer gateway (on-premises) side of the VPN connection.</p>"""
    remote_ipv6_network_cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv6 CIDR on the Amazon Web Services side of the VPN connection.</p>"""
    outside_ip_address_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The type of IPv4 address assigned to the outside interface of the customer gateway.</p> <p>Valid values: <code>PrivateIpv4</code> | <code>PublicIpv4</code> | <code>Ipv6</code> </p> <p>Default: <code>PublicIpv4</code> </p>"""
    transport_transit_gateway_attachment_id: NotRequired[
        "aws_sdk_ec2.types.string.String"
    ]
    """<p>The transit gateway attachment ID in use for the VPN tunnel.</p>"""
    tunnel_inside_ip_version: NotRequired[
        "aws_sdk_ec2.types.tunnel_inside_ip_version.TunnelInsideIpVersion"
    ]
    """<p>Indicates whether the VPN tunnels process IPv4 or IPv6 traffic.</p>"""
    tunnel_options: NotRequired[
        "aws_sdk_ec2.types.tunnel_options_list.TunnelOptionsList"
    ]
    """<p>Indicates the VPN tunnel options.</p>"""
    tunnel_bandwidth: NotRequired[
        "aws_sdk_ec2.types.vpn_tunnel_bandwidth.VpnTunnelBandwidth"
    ]
    """<p> The configured bandwidth for the VPN tunnel. Represents the current throughput capacity setting for the tunnel connection. <code>standard</code> tunnel bandwidth supports up to 1.25 Gbps per tunnel while <code>large</code> supports up to 5 Gbps per tunnel. If no tunnel bandwidth was specified for the connection, <code>standard</code> is used as the default value. </p>"""
