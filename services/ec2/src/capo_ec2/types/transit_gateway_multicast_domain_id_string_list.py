"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMulticastDomainIdStringList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_multicast_domain_id

TransitGatewayMulticastDomainIdStringList: TypeAlias = list[
    "capo_ec2.types.transit_gateway_multicast_domain_id.TransitGatewayMulticastDomainId"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayMulticastDomainIdStringList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_ec2_query(el: Element) -> TransitGatewayMulticastDomainIdStringList:
    out: TransitGatewayMulticastDomainIdStringList = []
    for child in el.findall("item"):
        out.append(str(child.text or ""))
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> TransitGatewayMulticastDomainIdStringList:
    out: TransitGatewayMulticastDomainIdStringList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
