"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitIntermediateStopList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_transit_intermediate_stop

RouteTransitIntermediateStopList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_transit_intermediate_stop.RouteTransitIntermediateStop"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitIntermediateStopList) -> list:
    import aws_sdk_geo_routes.types.route_transit_intermediate_stop

    out: list = []
    for item in value:
        out.append(
            aws_sdk_geo_routes.types.route_transit_intermediate_stop.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RouteTransitIntermediateStopList:
    import aws_sdk_geo_routes.types.route_transit_intermediate_stop

    out: RouteTransitIntermediateStopList = []
    for item in data:
        out.append(
            aws_sdk_geo_routes.types.route_transit_intermediate_stop.deserialize_json(
                item
            )
        )
    return out
