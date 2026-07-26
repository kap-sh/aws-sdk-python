"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.local_gateway_route_table_virtual_interface_group_association_set
    import capo_ec2.types.string


class DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResult(
    TypedDict, closed=True
):
    local_gateway_route_table_virtual_interface_group_associations: NotRequired[
        "capo_ec2.types.local_gateway_route_table_virtual_interface_group_association_set.LocalGatewayRouteTableVirtualInterfaceGroupAssociationSet"
    ]
    """<p>Information about the associations.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "local_gateway_route_table_virtual_interface_group_associations" in value:
        import capo_ec2.types.local_gateway_route_table_virtual_interface_group_association_set

        capo_ec2.types.local_gateway_route_table_virtual_interface_group_association_set.serialize_ec2_query(
            value["local_gateway_route_table_virtual_interface_group_associations"],
            pairs,
            f"{prefix}.LocalGatewayRouteTableVirtualInterfaceGroupAssociationSet",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(
    el: Element,
) -> DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResult:
    out: DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResult = {}  # type: ignore[typeddict-item]
    if el.find("LocalGatewayRouteTableVirtualInterfaceGroupAssociationSet") is not None:
        import capo_ec2.types.local_gateway_route_table_virtual_interface_group_association_set

        out["local_gateway_route_table_virtual_interface_group_associations"] = (
            capo_ec2.types.local_gateway_route_table_virtual_interface_group_association_set.deserialize_ec2_query(
                el, "LocalGatewayRouteTableVirtualInterfaceGroupAssociationSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
