"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteLocalGatewayRouteResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway_route


class DeleteLocalGatewayRouteResult(TypedDict, closed=True):
    route: NotRequired["aws_sdk_ec2.types.local_gateway_route.LocalGatewayRoute"]
    """<p>Information about the route.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteLocalGatewayRouteResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "route" in value:
        import aws_sdk_ec2.types.local_gateway_route

        aws_sdk_ec2.types.local_gateway_route.serialize_ec2_query(
            value["route"], pairs, f"{prefix}.Route"
        )


def deserialize_ec2_query(el: Element) -> DeleteLocalGatewayRouteResult:
    out: DeleteLocalGatewayRouteResult = {}  # type: ignore[typeddict-item]
    child_route = el.find("Route")
    if child_route is not None:
        import aws_sdk_ec2.types.local_gateway_route

        out["route"] = aws_sdk_ec2.types.local_gateway_route.deserialize_ec2_query(
            child_route
        )
    return out
