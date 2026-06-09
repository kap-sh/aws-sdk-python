"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_route_table_virtual_interface_group_association


class DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationResult(TypedDict):
    local_gateway_route_table_virtual_interface_group_association: NotRequired[
        "aws_sdk_ec2.types.local_gateway_route_table_virtual_interface_group_association.LocalGatewayRouteTableVirtualInterfaceGroupAssociation"
    ]
    """<p>Information about the association.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "local_gateway_route_table_virtual_interface_group_association" in value:
        import aws_sdk_ec2.types.local_gateway_route_table_virtual_interface_group_association

        aws_sdk_ec2.types.local_gateway_route_table_virtual_interface_group_association.serialize_ec2_query(
            value["local_gateway_route_table_virtual_interface_group_association"],
            pairs,
            f"{prefix}.LocalGatewayRouteTableVirtualInterfaceGroupAssociation",
        )


def deserialize_ec2_query(
    el: Element,
) -> DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationResult:
    out: DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationResult = {}  # type: ignore[typeddict-item]
    child_local_gateway_route_table_virtual_interface_group_association = el.find(
        "LocalGatewayRouteTableVirtualInterfaceGroupAssociation"
    )
    if child_local_gateway_route_table_virtual_interface_group_association is not None:
        import aws_sdk_ec2.types.local_gateway_route_table_virtual_interface_group_association

        out["local_gateway_route_table_virtual_interface_group_association"] = (
            aws_sdk_ec2.types.local_gateway_route_table_virtual_interface_group_association.deserialize_ec2_query(
                child_local_gateway_route_table_virtual_interface_group_association
            )
        )
    return out
