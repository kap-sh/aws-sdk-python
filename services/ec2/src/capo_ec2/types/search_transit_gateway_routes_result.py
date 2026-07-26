"""Generated from Smithy shape ``com.amazonaws.ec2#SearchTransitGatewayRoutesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.string
    import capo_ec2.types.transit_gateway_route_list


class SearchTransitGatewayRoutesResult(TypedDict, closed=True):
    routes: NotRequired[
        "capo_ec2.types.transit_gateway_route_list.TransitGatewayRouteList"
    ]
    """<p>Information about the routes.</p>"""
    additional_routes_available: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether there are additional routes available.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SearchTransitGatewayRoutesResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "routes" in value:
        import capo_ec2.types.transit_gateway_route_list

        capo_ec2.types.transit_gateway_route_list.serialize_ec2_query(
            value["routes"], pairs, f"{prefix}.RouteSet"
        )
    if "additional_routes_available" in value:
        pairs.append(
            (
                f"{prefix}.AdditionalRoutesAvailable",
                "true" if value["additional_routes_available"] else "false",
            )
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> SearchTransitGatewayRoutesResult:
    out: SearchTransitGatewayRoutesResult = {}  # type: ignore[typeddict-item]
    if el.find("RouteSet") is not None:
        import capo_ec2.types.transit_gateway_route_list

        out["routes"] = capo_ec2.types.transit_gateway_route_list.deserialize_ec2_query(
            el, "RouteSet"
        )
    child_additional_routes_available = el.find("AdditionalRoutesAvailable")
    if child_additional_routes_available is not None:
        out["additional_routes_available"] = (
            child_additional_routes_available.text or ""
        ).lower() == "true"
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
