"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteLocalGatewayRouteTableVpcAssociationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.local_gateway_route_table_vpc_association


class DeleteLocalGatewayRouteTableVpcAssociationResult(TypedDict, closed=True):
    local_gateway_route_table_vpc_association: NotRequired[
        "capo_ec2.types.local_gateway_route_table_vpc_association.LocalGatewayRouteTableVpcAssociation"
    ]
    """<p>Information about the association.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteLocalGatewayRouteTableVpcAssociationResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "local_gateway_route_table_vpc_association" in value:
        import capo_ec2.types.local_gateway_route_table_vpc_association

        capo_ec2.types.local_gateway_route_table_vpc_association.serialize_ec2_query(
            value["local_gateway_route_table_vpc_association"],
            pairs,
            f"{key_prefix}LocalGatewayRouteTableVpcAssociation",
        )


def deserialize_ec2_query(
    el: Element,
) -> DeleteLocalGatewayRouteTableVpcAssociationResult:
    out: DeleteLocalGatewayRouteTableVpcAssociationResult = {}  # type: ignore[typeddict-item]
    child_local_gateway_route_table_vpc_association = el.find(
        "LocalGatewayRouteTableVpcAssociation"
    )
    if child_local_gateway_route_table_vpc_association is not None:
        import capo_ec2.types.local_gateway_route_table_vpc_association

        out["local_gateway_route_table_vpc_association"] = (
            capo_ec2.types.local_gateway_route_table_vpc_association.deserialize_ec2_query(
                child_local_gateway_route_table_vpc_association
            )
        )
    return out
