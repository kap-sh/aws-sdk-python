"""Generated from Smithy shape ``com.amazonaws.ec2#VpnGatewayList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.vpn_gateway

VpnGatewayList: TypeAlias = list["capo_ec2.types.vpn_gateway.VpnGateway"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpnGatewayList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.vpn_gateway

        capo_ec2.types.vpn_gateway.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> VpnGatewayList:
    import capo_ec2.types.vpn_gateway

    out: VpnGatewayList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.vpn_gateway.deserialize_ec2_query(child))
    return out
