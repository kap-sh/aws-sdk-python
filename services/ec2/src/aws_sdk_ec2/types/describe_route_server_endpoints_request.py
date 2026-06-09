"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeRouteServerEndpointsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.filter_list
    import aws_sdk_ec2.types.route_server_endpoint_ids_list
    import aws_sdk_ec2.types.route_server_max_results
    import aws_sdk_ec2.types.string


class DescribeRouteServerEndpointsRequest(TypedDict):
    route_server_endpoint_ids: NotRequired[
        "aws_sdk_ec2.types.route_server_endpoint_ids_list.RouteServerEndpointIdsList"
    ]
    """<p>The IDs of the route server endpoints to describe.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token for the next page of results.</p>"""
    max_results: NotRequired[
        "aws_sdk_ec2.types.route_server_max_results.RouteServerMaxResults"
    ]
    """<p>The maximum number of results to return with a single call.</p>"""
    filters: NotRequired["aws_sdk_ec2.types.filter_list.FilterList"]
    """<p>One or more filters to apply to the describe request.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeRouteServerEndpointsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "route_server_endpoint_ids" in value:
        import aws_sdk_ec2.types.route_server_endpoint_ids_list

        aws_sdk_ec2.types.route_server_endpoint_ids_list.serialize_ec2_query(
            value["route_server_endpoint_ids"],
            pairs,
            f"{prefix}.RouteServerEndpointIds",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{prefix}.MaxResults", str(value["max_results"])))
    if "filters" in value:
        import aws_sdk_ec2.types.filter_list

        aws_sdk_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> DescribeRouteServerEndpointsRequest:
    out: DescribeRouteServerEndpointsRequest = {}  # type: ignore[typeddict-item]
    if el.find("RouteServerEndpointIds") is not None:
        import aws_sdk_ec2.types.route_server_endpoint_ids_list

        out["route_server_endpoint_ids"] = (
            aws_sdk_ec2.types.route_server_endpoint_ids_list.deserialize_ec2_query(
                el, "RouteServerEndpointIds"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    if el.find("Filters") is not None:
        import aws_sdk_ec2.types.filter_list

        out["filters"] = aws_sdk_ec2.types.filter_list.deserialize_ec2_query(
            el, "Filters"
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
