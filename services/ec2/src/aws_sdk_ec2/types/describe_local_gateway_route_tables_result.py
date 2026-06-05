"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeLocalGatewayRouteTablesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_route_table_set
    import aws_sdk_ec2.types.string


class DescribeLocalGatewayRouteTablesResult(TypedDict):
    local_gateway_route_tables: NotRequired[
        "aws_sdk_ec2.types.local_gateway_route_table_set.LocalGatewayRouteTableSet"
    ]
    """<p>Information about the local gateway route tables.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeLocalGatewayRouteTablesResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "local_gateway_route_tables" in value:
        import aws_sdk_ec2.types.local_gateway_route_table_set

        aws_sdk_ec2.types.local_gateway_route_table_set.serialize_ec2_query(
            value["local_gateway_route_tables"],
            pairs,
            f"{prefix}.LocalGatewayRouteTableSet",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeLocalGatewayRouteTablesResult:
    out: DescribeLocalGatewayRouteTablesResult = {}  # type: ignore[typeddict-item]
    if el.find("LocalGatewayRouteTableSet") is not None:
        import aws_sdk_ec2.types.local_gateway_route_table_set

        out["local_gateway_route_tables"] = (
            aws_sdk_ec2.types.local_gateway_route_table_set.deserialize_ec2_query(
                el, "LocalGatewayRouteTableSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
