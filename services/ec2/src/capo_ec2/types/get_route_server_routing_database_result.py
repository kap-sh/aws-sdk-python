"""Generated from Smithy shape ``com.amazonaws.ec2#GetRouteServerRoutingDatabaseResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.route_server_route_list
    import capo_ec2.types.string


class GetRouteServerRoutingDatabaseResult(TypedDict, closed=True):
    are_routes_persisted: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether routes are being persisted in the routing database.</p>"""
    routes: NotRequired["capo_ec2.types.route_server_route_list.RouteServerRouteList"]
    """<p>The collection of routes in the route server's routing database.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetRouteServerRoutingDatabaseResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "are_routes_persisted" in value:
        pairs.append(
            (
                f"{key_prefix}AreRoutesPersisted",
                "true" if value["are_routes_persisted"] else "false",
            )
        )
    if "routes" in value:
        import capo_ec2.types.route_server_route_list

        capo_ec2.types.route_server_route_list.serialize_ec2_query(
            value["routes"], pairs, f"{key_prefix}RouteSet"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetRouteServerRoutingDatabaseResult:
    out: GetRouteServerRoutingDatabaseResult = {}  # type: ignore[typeddict-item]
    child_are_routes_persisted = el.find("areRoutesPersisted")
    if child_are_routes_persisted is not None:
        out["are_routes_persisted"] = (
            child_are_routes_persisted.text or ""
        ).lower() == "true"
    child_routes = el.find("routeSet")
    if child_routes is not None:
        import capo_ec2.types.route_server_route_list

        out["routes"] = capo_ec2.types.route_server_route_list.deserialize_ec2_query(
            child_routes
        )
    child_next_token = el.find("nextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
