"""Generated from Smithy shape ``com.amazonaws.ec2#CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.local_gateway_route_table_virtual_interface_group_association


class CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationResult(
    TypedDict, closed=True
):
    local_gateway_route_table_virtual_interface_group_association: NotRequired[
        "capo_ec2.types.local_gateway_route_table_virtual_interface_group_association.LocalGatewayRouteTableVirtualInterfaceGroupAssociation"
    ]
    """<p>Information about the local gateway route table virtual interface group association.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "local_gateway_route_table_virtual_interface_group_association" in value:
        import capo_ec2.types.local_gateway_route_table_virtual_interface_group_association

        capo_ec2.types.local_gateway_route_table_virtual_interface_group_association.serialize_ec2_query(
            value["local_gateway_route_table_virtual_interface_group_association"],
            pairs,
            f"{key_prefix}LocalGatewayRouteTableVirtualInterfaceGroupAssociation",
        )


def deserialize_ec2_query(
    el: Element,
) -> CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationResult:
    out: CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationResult = {}  # type: ignore[typeddict-item]
    child_local_gateway_route_table_virtual_interface_group_association = el.find(
        "LocalGatewayRouteTableVirtualInterfaceGroupAssociation"
    )
    if child_local_gateway_route_table_virtual_interface_group_association is not None:
        import capo_ec2.types.local_gateway_route_table_virtual_interface_group_association

        out["local_gateway_route_table_virtual_interface_group_association"] = (
            capo_ec2.types.local_gateway_route_table_virtual_interface_group_association.deserialize_ec2_query(
                child_local_gateway_route_table_virtual_interface_group_association
            )
        )
    return out
