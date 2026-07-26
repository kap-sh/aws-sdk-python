"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTransitGatewayRouteResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_route


class DeleteTransitGatewayRouteResult(TypedDict, closed=True):
    route: NotRequired["capo_ec2.types.transit_gateway_route.TransitGatewayRoute"]
    """<p>Information about the route.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteTransitGatewayRouteResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "route" in value:
        import capo_ec2.types.transit_gateway_route

        capo_ec2.types.transit_gateway_route.serialize_ec2_query(
            value["route"], pairs, f"{prefix}.Route"
        )


def deserialize_ec2_query(el: Element) -> DeleteTransitGatewayRouteResult:
    out: DeleteTransitGatewayRouteResult = {}  # type: ignore[typeddict-item]
    child_route = el.find("Route")
    if child_route is not None:
        import capo_ec2.types.transit_gateway_route

        out["route"] = capo_ec2.types.transit_gateway_route.deserialize_ec2_query(
            child_route
        )
    return out
