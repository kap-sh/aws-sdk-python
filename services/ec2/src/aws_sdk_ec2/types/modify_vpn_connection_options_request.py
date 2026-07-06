"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpnConnectionOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpn_connection_id
    import aws_sdk_ec2.types.vpn_tunnel_bandwidth


class ModifyVpnConnectionOptionsRequest(TypedDict, closed=True):
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


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVpnConnectionOptionsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "vpn_connection_id" in value:
        pairs.append((f"{prefix}.VpnConnectionId", str(value["vpn_connection_id"])))
    if "local_ipv4_network_cidr" in value:
        pairs.append(
            (f"{prefix}.LocalIpv4NetworkCidr", str(value["local_ipv4_network_cidr"]))
        )
    if "remote_ipv4_network_cidr" in value:
        pairs.append(
            (f"{prefix}.RemoteIpv4NetworkCidr", str(value["remote_ipv4_network_cidr"]))
        )
    if "local_ipv6_network_cidr" in value:
        pairs.append(
            (f"{prefix}.LocalIpv6NetworkCidr", str(value["local_ipv6_network_cidr"]))
        )
    if "remote_ipv6_network_cidr" in value:
        pairs.append(
            (f"{prefix}.RemoteIpv6NetworkCidr", str(value["remote_ipv6_network_cidr"]))
        )
    if "tunnel_bandwidth" in value:
        import aws_sdk_ec2.types.vpn_tunnel_bandwidth

        aws_sdk_ec2.types.vpn_tunnel_bandwidth.serialize_ec2_query(
            value["tunnel_bandwidth"], pairs, f"{prefix}.TunnelBandwidth"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> ModifyVpnConnectionOptionsRequest:
    out: ModifyVpnConnectionOptionsRequest = {}  # type: ignore[typeddict-item]
    child_vpn_connection_id = el.find("VpnConnectionId")
    if child_vpn_connection_id is not None:
        out["vpn_connection_id"] = str(child_vpn_connection_id.text or "")
    child_local_ipv4_network_cidr = el.find("LocalIpv4NetworkCidr")
    if child_local_ipv4_network_cidr is not None:
        out["local_ipv4_network_cidr"] = str(child_local_ipv4_network_cidr.text or "")
    child_remote_ipv4_network_cidr = el.find("RemoteIpv4NetworkCidr")
    if child_remote_ipv4_network_cidr is not None:
        out["remote_ipv4_network_cidr"] = str(child_remote_ipv4_network_cidr.text or "")
    child_local_ipv6_network_cidr = el.find("LocalIpv6NetworkCidr")
    if child_local_ipv6_network_cidr is not None:
        out["local_ipv6_network_cidr"] = str(child_local_ipv6_network_cidr.text or "")
    child_remote_ipv6_network_cidr = el.find("RemoteIpv6NetworkCidr")
    if child_remote_ipv6_network_cidr is not None:
        out["remote_ipv6_network_cidr"] = str(child_remote_ipv6_network_cidr.text or "")
    child_tunnel_bandwidth = el.find("TunnelBandwidth")
    if child_tunnel_bandwidth is not None:
        import aws_sdk_ec2.types.vpn_tunnel_bandwidth

        out["tunnel_bandwidth"] = (
            aws_sdk_ec2.types.vpn_tunnel_bandwidth.deserialize_ec2_query(
                child_tunnel_bandwidth
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
