"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVpnGatewayResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.vpn_gateway


class CreateVpnGatewayResult(TypedDict, closed=True):
    vpn_gateway: NotRequired["capo_ec2.types.vpn_gateway.VpnGateway"]
    """<p>Information about the virtual private gateway.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateVpnGatewayResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "vpn_gateway" in value:
        import capo_ec2.types.vpn_gateway

        capo_ec2.types.vpn_gateway.serialize_ec2_query(
            value["vpn_gateway"], pairs, f"{key_prefix}VpnGateway"
        )


def deserialize_ec2_query(el: Element) -> CreateVpnGatewayResult:
    out: CreateVpnGatewayResult = {}  # type: ignore[typeddict-item]
    child_vpn_gateway = el.find("vpnGateway")
    if child_vpn_gateway is not None:
        import capo_ec2.types.vpn_gateway

        out["vpn_gateway"] = capo_ec2.types.vpn_gateway.deserialize_ec2_query(
            child_vpn_gateway
        )
    return out
