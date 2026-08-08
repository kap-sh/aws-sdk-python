"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeRouteServersResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.route_servers_list
    import capo_ec2.types.string


class DescribeRouteServersResult(TypedDict, closed=True):
    route_servers: NotRequired["capo_ec2.types.route_servers_list.RouteServersList"]
    """<p>Information about the described route servers.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeRouteServersResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "route_servers" in value:
        import capo_ec2.types.route_servers_list

        capo_ec2.types.route_servers_list.serialize_ec2_query(
            value["route_servers"], pairs, f"{key_prefix}RouteServerSet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeRouteServersResult:
    out: DescribeRouteServersResult = {}  # type: ignore[typeddict-item]
    if el.find("routeServerSet") is not None:
        import capo_ec2.types.route_servers_list

        out["route_servers"] = capo_ec2.types.route_servers_list.deserialize_ec2_query(
            el, "routeServerSet"
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
