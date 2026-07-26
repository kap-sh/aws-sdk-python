"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway

TransitGatewayList: TypeAlias = list["capo_ec2.types.transit_gateway.TransitGateway"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.transit_gateway

        capo_ec2.types.transit_gateway.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> TransitGatewayList:
    import capo_ec2.types.transit_gateway

    out: TransitGatewayList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.transit_gateway.deserialize_ec2_query(child))
    return out
