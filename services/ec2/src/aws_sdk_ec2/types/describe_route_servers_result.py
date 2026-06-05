"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeRouteServersResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.route_servers_list
    import aws_sdk_ec2.types.string


class DescribeRouteServersResult(TypedDict):
    route_servers: NotRequired["aws_sdk_ec2.types.route_servers_list.RouteServersList"]
    """<p>Information about the described route servers.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeRouteServersResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "route_servers" in value:
        import aws_sdk_ec2.types.route_servers_list

        aws_sdk_ec2.types.route_servers_list.serialize_ec2_query(
            value["route_servers"], pairs, f"{prefix}.RouteServerSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeRouteServersResult:
    out: DescribeRouteServersResult = {}  # type: ignore[typeddict-item]
    if el.find("RouteServerSet") is not None:
        import aws_sdk_ec2.types.route_servers_list

        out["route_servers"] = (
            aws_sdk_ec2.types.route_servers_list.deserialize_ec2_query(
                el, "RouteServerSet"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
