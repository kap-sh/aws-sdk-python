"""Generated from Smithy shape ``com.amazonaws.ec2#GetActiveVpnTunnelStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.string
    import capo_ec2.types.vpn_connection_id


class GetActiveVpnTunnelStatusRequest(TypedDict, closed=True):
    vpn_connection_id: NotRequired["capo_ec2.types.vpn_connection_id.VpnConnectionId"]
    """<p>The ID of the VPN connection for which to retrieve the active tunnel status.</p>"""
    vpn_tunnel_outside_ip_address: NotRequired["capo_ec2.types.string.String"]
    """<p>The external IP address of the VPN tunnel for which to retrieve the active status.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetActiveVpnTunnelStatusRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "vpn_connection_id" in value:
        pairs.append((f"{key_prefix}VpnConnectionId", str(value["vpn_connection_id"])))
    if "vpn_tunnel_outside_ip_address" in value:
        pairs.append(
            (
                f"{key_prefix}VpnTunnelOutsideIpAddress",
                str(value["vpn_tunnel_outside_ip_address"]),
            )
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> GetActiveVpnTunnelStatusRequest:
    out: GetActiveVpnTunnelStatusRequest = {}  # type: ignore[typeddict-item]
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
