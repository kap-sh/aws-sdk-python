"""Generated from Smithy shape ``com.amazonaws.ec2#LocalGatewayRouteTableVirtualInterfaceGroupAssociationSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.local_gateway_route_table_virtual_interface_group_association

LocalGatewayRouteTableVirtualInterfaceGroupAssociationSet: TypeAlias = list[
    "capo_ec2.types.local_gateway_route_table_virtual_interface_group_association.LocalGatewayRouteTableVirtualInterfaceGroupAssociation"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LocalGatewayRouteTableVirtualInterfaceGroupAssociationSet,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.local_gateway_route_table_virtual_interface_group_association

        capo_ec2.types.local_gateway_route_table_virtual_interface_group_association.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    el: Element,
) -> LocalGatewayRouteTableVirtualInterfaceGroupAssociationSet:
    import capo_ec2.types.local_gateway_route_table_virtual_interface_group_association

    out: LocalGatewayRouteTableVirtualInterfaceGroupAssociationSet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.local_gateway_route_table_virtual_interface_group_association.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> LocalGatewayRouteTableVirtualInterfaceGroupAssociationSet:
    import capo_ec2.types.local_gateway_route_table_virtual_interface_group_association

    out: LocalGatewayRouteTableVirtualInterfaceGroupAssociationSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.local_gateway_route_table_virtual_interface_group_association.deserialize_ec2_query(
                child
            )
        )
    return out
