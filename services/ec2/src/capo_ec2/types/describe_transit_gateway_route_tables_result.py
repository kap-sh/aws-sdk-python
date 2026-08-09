"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeTransitGatewayRouteTablesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.transit_gateway_route_table_list


class DescribeTransitGatewayRouteTablesResult(TypedDict, closed=True):
    transit_gateway_route_tables: NotRequired[
        "capo_ec2.types.transit_gateway_route_table_list.TransitGatewayRouteTableList"
    ]
    """<p>Information about the transit gateway route tables.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeTransitGatewayRouteTablesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_route_tables" in value:
        import capo_ec2.types.transit_gateway_route_table_list

        capo_ec2.types.transit_gateway_route_table_list.serialize_ec2_query(
            value["transit_gateway_route_tables"],
            pairs,
            f"{key_prefix}TransitGatewayRouteTables",
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeTransitGatewayRouteTablesResult:
    out: DescribeTransitGatewayRouteTablesResult = {}  # type: ignore[typeddict-item]
    child_transit_gateway_route_tables = el.find("transitGatewayRouteTables")
    if child_transit_gateway_route_tables is not None:
        import capo_ec2.types.transit_gateway_route_table_list

        out["transit_gateway_route_tables"] = (
            capo_ec2.types.transit_gateway_route_table_list.deserialize_ec2_query(
                child_transit_gateway_route_tables
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
