"""Generated from Smithy shape ``com.amazonaws.ec2#GetActiveVpnTunnelStatusResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.active_vpn_tunnel_status


class GetActiveVpnTunnelStatusResult(TypedDict, closed=True):
    active_vpn_tunnel_status: NotRequired[
        "capo_ec2.types.active_vpn_tunnel_status.ActiveVpnTunnelStatus"
    ]
    """<p>Information about the current security configuration of the VPN tunnel.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetActiveVpnTunnelStatusResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "active_vpn_tunnel_status" in value:
        import capo_ec2.types.active_vpn_tunnel_status

        capo_ec2.types.active_vpn_tunnel_status.serialize_ec2_query(
            value["active_vpn_tunnel_status"],
            pairs,
            f"{key_prefix}ActiveVpnTunnelStatus",
        )


def deserialize_ec2_query(el: Element) -> GetActiveVpnTunnelStatusResult:
    out: GetActiveVpnTunnelStatusResult = {}  # type: ignore[typeddict-item]
    child_active_vpn_tunnel_status = el.find("activeVpnTunnelStatus")
    if child_active_vpn_tunnel_status is not None:
        import capo_ec2.types.active_vpn_tunnel_status

        out["active_vpn_tunnel_status"] = (
            capo_ec2.types.active_vpn_tunnel_status.deserialize_ec2_query(
                child_active_vpn_tunnel_status
            )
        )
    return out
