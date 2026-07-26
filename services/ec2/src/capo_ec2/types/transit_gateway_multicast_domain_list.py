"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMulticastDomainList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_multicast_domain

TransitGatewayMulticastDomainList: TypeAlias = list[
    "capo_ec2.types.transit_gateway_multicast_domain.TransitGatewayMulticastDomain"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayMulticastDomainList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.transit_gateway_multicast_domain

        capo_ec2.types.transit_gateway_multicast_domain.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> TransitGatewayMulticastDomainList:
    import capo_ec2.types.transit_gateway_multicast_domain

    out: TransitGatewayMulticastDomainList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.transit_gateway_multicast_domain.deserialize_ec2_query(child)
        )
    return out
