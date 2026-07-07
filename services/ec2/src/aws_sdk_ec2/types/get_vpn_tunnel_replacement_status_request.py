"""Generated from Smithy shape ``com.amazonaws.ec2#GetVpnTunnelReplacementStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpn_connection_id


class GetVpnTunnelReplacementStatusRequest(TypedDict, closed=True):
    vpn_connection_id: NotRequired[
        "aws_sdk_ec2.types.vpn_connection_id.VpnConnectionId"
    ]
    """<p>The ID of the Site-to-Site VPN connection. </p>"""
    vpn_tunnel_outside_ip_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The external IP address of the VPN tunnel.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetVpnTunnelReplacementStatusRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "vpn_connection_id" in value:
        pairs.append((f"{prefix}.VpnConnectionId", str(value["vpn_connection_id"])))
    if "vpn_tunnel_outside_ip_address" in value:
        pairs.append(
            (
                f"{prefix}.VpnTunnelOutsideIpAddress",
                str(value["vpn_tunnel_outside_ip_address"]),
            )
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> GetVpnTunnelReplacementStatusRequest:
    out: GetVpnTunnelReplacementStatusRequest = {}  # type: ignore[typeddict-item]
    child_vpn_connection_id = el.find("VpnConnectionId")
    if child_vpn_connection_id is not None:
        out["vpn_connection_id"] = str(child_vpn_connection_id.text or "")
    child_vpn_tunnel_outside_ip_address = el.find("VpnTunnelOutsideIpAddress")
    if child_vpn_tunnel_outside_ip_address is not None:
        out["vpn_tunnel_outside_ip_address"] = str(
            child_vpn_tunnel_outside_ip_address.text or ""
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
