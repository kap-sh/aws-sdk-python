"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitNextDepartureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_transit_next_departure

RouteTransitNextDepartureList: TypeAlias = list[
    "aws_sdk_geo_routes.types.route_transit_next_departure.RouteTransitNextDeparture"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitNextDepartureList) -> list:
    import aws_sdk_geo_routes.types.route_transit_next_departure

    out: list = []
    for item in value:
        out.append(
            aws_sdk_geo_routes.types.route_transit_next_departure.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouteTransitNextDepartureList:
    import aws_sdk_geo_routes.types.route_transit_next_departure

    out: RouteTransitNextDepartureList = []
    for item in data:
        out.append(
            aws_sdk_geo_routes.types.route_transit_next_departure.deserialize_json(item)
        )
    return out
