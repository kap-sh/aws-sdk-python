"""Generated from Smithy shape ``com.amazonaws.ec2#LocalGatewayRouteTableVirtualInterfaceGroupAssociationIdSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.local_gateway_route_table_virtual_interface_group_association_id

LocalGatewayRouteTableVirtualInterfaceGroupAssociationIdSet: TypeAlias = list[
    "capo_ec2.types.local_gateway_route_table_virtual_interface_group_association_id.LocalGatewayRouteTableVirtualInterfaceGroupAssociationId"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LocalGatewayRouteTableVirtualInterfaceGroupAssociationIdSet,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_ec2_query(
    el: Element,
) -> LocalGatewayRouteTableVirtualInterfaceGroupAssociationIdSet:
    out: LocalGatewayRouteTableVirtualInterfaceGroupAssociationIdSet = []
    for child in el.findall("item"):
        out.append(str(child.text or ""))
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> LocalGatewayRouteTableVirtualInterfaceGroupAssociationIdSet:
    out: LocalGatewayRouteTableVirtualInterfaceGroupAssociationIdSet = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
