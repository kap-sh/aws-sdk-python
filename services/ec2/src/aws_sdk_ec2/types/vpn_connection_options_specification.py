"""Generated from Smithy shape ``com.amazonaws.ec2#VpnConnectionOptionsSpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_attachment_id
    import aws_sdk_ec2.types.tunnel_inside_ip_version
    import aws_sdk_ec2.types.vpn_tunnel_bandwidth
    import aws_sdk_ec2.types.vpn_tunnel_options_specifications_list


class VpnConnectionOptionsSpecification(TypedDict):
    enable_acceleration: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicate whether to enable acceleration for the VPN connection.</p> <p>Default: <code>false</code> </p>"""
    tunnel_inside_ip_version: NotRequired[
        "aws_sdk_ec2.types.tunnel_inside_ip_version.TunnelInsideIpVersion"
    ]
    """<p>Indicate whether the VPN tunnels process IPv4 or IPv6 traffic.</p> <p>Default: <code>ipv4</code> </p>"""
    tunnel_options: NotRequired[
        "aws_sdk_ec2.types.vpn_tunnel_options_specifications_list.VpnTunnelOptionsSpecificationsList"
    ]
    """<p>The tunnel options for the VPN connection.</p>"""
    local_ipv4_network_cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 CIDR on the customer gateway (on-premises) side of the VPN connection.</p> <p>Default: <code>0.0.0.0/0</code> </p>"""
    remote_ipv4_network_cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv4 CIDR on the Amazon Web Services side of the VPN connection.</p> <p>Default: <code>0.0.0.0/0</code> </p>"""
    local_ipv6_network_cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv6 CIDR on the customer gateway (on-premises) side of the VPN connection.</p> <p>Default: <code>::/0</code> </p>"""
    remote_ipv6_network_cidr: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The IPv6 CIDR on the Amazon Web Services side of the VPN connection.</p> <p>Default: <code>::/0</code> </p>"""
    outside_ip_address_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The type of IP address assigned to the outside interface of the customer gateway device.</p> <p>Valid values: <code>PrivateIpv4</code> | <code>PublicIpv4</code> | <code>Ipv6</code> </p> <p>Default: <code>PublicIpv4</code> </p>"""
    transport_transit_gateway_attachment_id: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The transit gateway attachment ID to use for the VPN tunnel.</p> <p>Required if <code>OutsideIpAddressType</code> is set to <code>PrivateIpv4</code>.</p>"""
    tunnel_bandwidth: NotRequired[
        "aws_sdk_ec2.types.vpn_tunnel_bandwidth.VpnTunnelBandwidth"
    ]
    """<p> The desired bandwidth specification for the VPN tunnel, used when creating or modifying VPN connection options to set the tunnel's throughput capacity. <code>standard</code> supports up to 1.25 Gbps per tunnel, while <code>large</code> supports up to 5 Gbps per tunnel. The default value is <code>standard</code>. Existing VPN connections without a bandwidth setting will automatically default to <code>standard</code>. </p>"""
    static_routes_only: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicate whether the VPN connection uses static routes only. If you are creating a VPN connection for a device that does not support BGP, you must specify <code>true</code>. Use <a>CreateVpnConnectionRoute</a> to create a static route.</p> <p>Default: <code>false</code> </p>"""
