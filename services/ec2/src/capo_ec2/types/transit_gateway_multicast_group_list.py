"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMulticastGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_multicast_group

TransitGatewayMulticastGroupList: TypeAlias = list[
    "capo_ec2.types.transit_gateway_multicast_group.TransitGatewayMulticastGroup"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayMulticastGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.transit_gateway_multicast_group

        capo_ec2.types.transit_gateway_multicast_group.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayMulticastGroupList:
    import capo_ec2.types.transit_gateway_multicast_group

    out: TransitGatewayMulticastGroupList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.transit_gateway_multicast_group.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> TransitGatewayMulticastGroupList:
    import capo_ec2.types.transit_gateway_multicast_group

    out: TransitGatewayMulticastGroupList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.transit_gateway_multicast_group.deserialize_ec2_query(child)
        )
    return out
