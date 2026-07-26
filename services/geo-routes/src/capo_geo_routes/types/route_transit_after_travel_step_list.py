"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitAfterTravelStepList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_transit_after_travel_step

RouteTransitAfterTravelStepList: TypeAlias = list[
    "capo_geo_routes.types.route_transit_after_travel_step.RouteTransitAfterTravelStep"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitAfterTravelStepList) -> list:
    import capo_geo_routes.types.route_transit_after_travel_step

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.route_transit_after_travel_step.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouteTransitAfterTravelStepList:
    import capo_geo_routes.types.route_transit_after_travel_step

    out: RouteTransitAfterTravelStepList = []
    for item in data:
        out.append(
            capo_geo_routes.types.route_transit_after_travel_step.deserialize_json(item)
        )
    return out
