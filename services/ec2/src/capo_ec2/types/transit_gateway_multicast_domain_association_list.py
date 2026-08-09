"""Generated from Smithy shape ``com.amazonaws.ec2#TransitGatewayMulticastDomainAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_multicast_domain_association

TransitGatewayMulticastDomainAssociationList: TypeAlias = list[
    "capo_ec2.types.transit_gateway_multicast_domain_association.TransitGatewayMulticastDomainAssociation"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TransitGatewayMulticastDomainAssociationList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.transit_gateway_multicast_domain_association

        capo_ec2.types.transit_gateway_multicast_domain_association.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> TransitGatewayMulticastDomainAssociationList:
    import capo_ec2.types.transit_gateway_multicast_domain_association

    out: TransitGatewayMulticastDomainAssociationList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.transit_gateway_multicast_domain_association.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> TransitGatewayMulticastDomainAssociationList:
    import capo_ec2.types.transit_gateway_multicast_domain_association

    out: TransitGatewayMulticastDomainAssociationList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.transit_gateway_multicast_domain_association.deserialize_ec2_query(
                child
            )
        )
    return out
