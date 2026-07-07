"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeLocalGatewayRouteTablesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.local_gateway_max_results
    import aws_sdk_ec2.types.local_gateway_route_table_id_set
    import aws_sdk_ec2.types.string


class DescribeLocalGatewayRouteTablesRequest(TypedDict, closed=True):
    local_gateway_route_table_ids: NotRequired[
        "aws_sdk_ec2.types.local_gateway_route_table_id_set.LocalGatewayRouteTableIdSet"
    ]
    """<p>The IDs of the local gateway route tables.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters.</p> <ul> <li> <p> <code>local-gateway-id</code> - The ID of a local gateway.</p> </li> <li> <p> <code>local-gateway-route-table-arn</code> - The Amazon Resource Name (ARN) of the local gateway route table.</p> </li> <li> <p> <code>local-gateway-route-table-id</code> - The ID of a local gateway route table.</p> </li> <li> <p> <code>outpost-arn</code> - The Amazon Resource Name (ARN) of the Outpost.</p> </li> <li> <p> <code>owner-id</code> - The ID of the Amazon Web Services account that owns the local gateway route table.</p> </li> <li> <p> <code>state</code> - The state of the local gateway route table.</p> </li> </ul>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.local_gateway_max_results.LocalGatewayMaxResults"
    ]
    """<p>The maximum number of results to return with a single call. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token for the next page of results.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeLocalGatewayRouteTablesRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "local_gateway_route_table_ids" in value:
        import aws_sdk_ec2.types.local_gateway_route_table_id_set

        aws_sdk_ec2.types.local_gateway_route_table_id_set.serialize_ec2_query(
            value["local_gateway_route_table_ids"],
            pairs,
            f"{prefix}.LocalGatewayRouteTableIds",
        )
    if "filters" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DescribeLocalGatewayRouteTablesRequest:
    out: DescribeLocalGatewayRouteTablesRequest = {}  # type: ignore[typeddict-item]
    if el.find("LocalGatewayRouteTableIds") is not None:
        import aws_sdk_ec2.types.local_gateway_route_table_id_set

        out["local_gateway_route_table_ids"] = (
            aws_sdk_ec2.types.local_gateway_route_table_id_set.deserialize_ec2_query(
                el, "LocalGatewayRouteTableIds"
            )
        )
    if el.find("Filters") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filters"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filters"
        )
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
