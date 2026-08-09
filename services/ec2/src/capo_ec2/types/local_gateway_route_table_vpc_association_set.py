"""Generated from Smithy shape ``com.amazonaws.ec2#LocalGatewayRouteTableVpcAssociationSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.local_gateway_route_table_vpc_association

LocalGatewayRouteTableVpcAssociationSet: TypeAlias = list[
    "capo_ec2.types.local_gateway_route_table_vpc_association.LocalGatewayRouteTableVpcAssociation"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LocalGatewayRouteTableVpcAssociationSet,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.local_gateway_route_table_vpc_association

        capo_ec2.types.local_gateway_route_table_vpc_association.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> LocalGatewayRouteTableVpcAssociationSet:
    import capo_ec2.types.local_gateway_route_table_vpc_association

    out: LocalGatewayRouteTableVpcAssociationSet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.local_gateway_route_table_vpc_association.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> LocalGatewayRouteTableVpcAssociationSet:
    import capo_ec2.types.local_gateway_route_table_vpc_association

    out: LocalGatewayRouteTableVpcAssociationSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.local_gateway_route_table_vpc_association.deserialize_ec2_query(
                child
            )
        )
    return out
