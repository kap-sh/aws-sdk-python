"""Generated from Smithy shape ``com.amazonaws.ec2#GetRouteServerRoutingDatabaseResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.route_server_route_list
    import aws_sdk_ec2.types.string


class GetRouteServerRoutingDatabaseResult(TypedDict):
    are_routes_persisted: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether routes are being persisted in the routing database.</p>"""
    routes: NotRequired[
        "aws_sdk_ec2.types.route_server_route_list.RouteServerRouteList"
    ]
    """<p>The collection of routes in the route server's routing database.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetRouteServerRoutingDatabaseResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "are_routes_persisted" in value:
        pairs.append(
            (
                f"{prefix}.AreRoutesPersisted",
                "true" if value["are_routes_persisted"] else "false",
            )
        )
    if "routes" in value:
        import aws_sdk_ec2.types.route_server_route_list

        aws_sdk_ec2.types.route_server_route_list.serialize_ec2_query(
            value["routes"], pairs, f"{prefix}.RouteSet"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> GetRouteServerRoutingDatabaseResult:
    out: GetRouteServerRoutingDatabaseResult = {}  # type: ignore[typeddict-item]
    child_are_routes_persisted = el.find("AreRoutesPersisted")
    if child_are_routes_persisted is not None:
        out["are_routes_persisted"] = (
            child_are_routes_persisted.text or ""
        ).lower() == "true"
    if el.find("RouteSet") is not None:
        import aws_sdk_ec2.types.route_server_route_list

        out["routes"] = aws_sdk_ec2.types.route_server_route_list.deserialize_ec2_query(
            el, "RouteSet"
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
