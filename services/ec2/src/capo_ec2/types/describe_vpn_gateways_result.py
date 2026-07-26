"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpnGatewaysResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.vpn_gateway_list


class DescribeVpnGatewaysResult(TypedDict, closed=True):
    vpn_gateways: NotRequired["capo_ec2.types.vpn_gateway_list.VpnGatewayList"]
    """<p>Information about one or more virtual private gateways.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpnGatewaysResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "vpn_gateways" in value:
        import capo_ec2.types.vpn_gateway_list

        capo_ec2.types.vpn_gateway_list.serialize_ec2_query(
            value["vpn_gateways"], pairs, f"{prefix}.VpnGatewaySet"
        )


def deserialize_ec2_query(el: Element) -> DescribeVpnGatewaysResult:
    out: DescribeVpnGatewaysResult = {}  # type: ignore[typeddict-item]
    if el.find("VpnGatewaySet") is not None:
        import capo_ec2.types.vpn_gateway_list

        out["vpn_gateways"] = capo_ec2.types.vpn_gateway_list.deserialize_ec2_query(
            el, "VpnGatewaySet"
        )
    return out
