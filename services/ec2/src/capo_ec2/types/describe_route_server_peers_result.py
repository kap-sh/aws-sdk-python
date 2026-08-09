"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeRouteServerPeersResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.route_server_peers_list
    import capo_ec2.types.string


class DescribeRouteServerPeersResult(TypedDict, closed=True):
    route_server_peers: NotRequired[
        "capo_ec2.types.route_server_peers_list.RouteServerPeersList"
    ]
    """<p>Information about the described route server peers.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeRouteServerPeersResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "route_server_peers" in value:
        import capo_ec2.types.route_server_peers_list

        capo_ec2.types.route_server_peers_list.serialize_ec2_query(
            value["route_server_peers"], pairs, f"{key_prefix}RouteServerPeerSet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeRouteServerPeersResult:
    out: DescribeRouteServerPeersResult = {}  # type: ignore[typeddict-item]
    child_route_server_peers = el.find("routeServerPeerSet")
    if child_route_server_peers is not None:
        import capo_ec2.types.route_server_peers_list

        out["route_server_peers"] = (
            capo_ec2.types.route_server_peers_list.deserialize_ec2_query(
                child_route_server_peers
            )
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
