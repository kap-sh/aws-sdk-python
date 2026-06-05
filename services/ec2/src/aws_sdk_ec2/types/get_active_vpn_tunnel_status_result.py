"""Generated from Smithy shape ``com.amazonaws.ec2#GetActiveVpnTunnelStatusResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.active_vpn_tunnel_status


class GetActiveVpnTunnelStatusResult(TypedDict):
    active_vpn_tunnel_status: NotRequired[
        "aws_sdk_ec2.types.active_vpn_tunnel_status.ActiveVpnTunnelStatus"
    ]
    """<p>Information about the current security configuration of the VPN tunnel.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetActiveVpnTunnelStatusResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "active_vpn_tunnel_status" in value:
        import aws_sdk_ec2.types.active_vpn_tunnel_status

        aws_sdk_ec2.types.active_vpn_tunnel_status.serialize_ec2_query(
            value["active_vpn_tunnel_status"], pairs, f"{prefix}.ActiveVpnTunnelStatus"
        )


def deserialize_ec2_query(el: Element) -> GetActiveVpnTunnelStatusResult:
    out: GetActiveVpnTunnelStatusResult = {}  # type: ignore[typeddict-item]
    child_active_vpn_tunnel_status = el.find("ActiveVpnTunnelStatus")
    if child_active_vpn_tunnel_status is not None:
        import aws_sdk_ec2.types.active_vpn_tunnel_status

        out["active_vpn_tunnel_status"] = (
            aws_sdk_ec2.types.active_vpn_tunnel_status.deserialize_ec2_query(
                child_active_vpn_tunnel_status
            )
        )
    return out
