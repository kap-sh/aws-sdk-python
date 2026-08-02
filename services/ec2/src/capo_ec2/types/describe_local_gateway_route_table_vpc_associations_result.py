"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeLocalGatewayRouteTableVpcAssociationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.local_gateway_route_table_vpc_association_set
    import capo_ec2.types.string


class DescribeLocalGatewayRouteTableVpcAssociationsResult(TypedDict, closed=True):
    local_gateway_route_table_vpc_associations: NotRequired[
        "capo_ec2.types.local_gateway_route_table_vpc_association_set.LocalGatewayRouteTableVpcAssociationSet"
    ]
    """<p>Information about the associations.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeLocalGatewayRouteTableVpcAssociationsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "local_gateway_route_table_vpc_associations" in value:
        import capo_ec2.types.local_gateway_route_table_vpc_association_set

        capo_ec2.types.local_gateway_route_table_vpc_association_set.serialize_ec2_query(
            value["local_gateway_route_table_vpc_associations"],
            pairs,
            f"{key_prefix}LocalGatewayRouteTableVpcAssociationSet",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(
    el: Element,
) -> DescribeLocalGatewayRouteTableVpcAssociationsResult:
    out: DescribeLocalGatewayRouteTableVpcAssociationsResult = {}  # type: ignore[typeddict-item]
    if el.find("LocalGatewayRouteTableVpcAssociationSet") is not None:
        import capo_ec2.types.local_gateway_route_table_vpc_association_set

        out["local_gateway_route_table_vpc_associations"] = (
            capo_ec2.types.local_gateway_route_table_vpc_association_set.deserialize_ec2_query(
                el, "LocalGatewayRouteTableVpcAssociationSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
