"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeRouteServerEndpointsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_server_endpoints_list
    import aws_sdk_ec2.types.string


class DescribeRouteServerEndpointsResult(TypedDict):
    route_server_endpoints: NotRequired[
        "aws_sdk_ec2.types.route_server_endpoints_list.RouteServerEndpointsList"
    ]
    """<p>Information about the described route server endpoints.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeRouteServerEndpointsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "route_server_endpoints" in value:
        import aws_sdk_ec2.types.route_server_endpoints_list

        aws_sdk_ec2.types.route_server_endpoints_list.serialize_ec2_query(
            value["route_server_endpoints"], pairs, f"{prefix}.RouteServerEndpointSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeRouteServerEndpointsResult:
    out: DescribeRouteServerEndpointsResult = {}  # type: ignore[typeddict-item]
    if el.find("RouteServerEndpointSet") is not None:
        import aws_sdk_ec2.types.route_server_endpoints_list

        out["route_server_endpoints"] = (
            aws_sdk_ec2.types.route_server_endpoints_list.deserialize_ec2_query(
                el, "RouteServerEndpointSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
