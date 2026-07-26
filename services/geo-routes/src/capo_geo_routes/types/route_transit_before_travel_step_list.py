"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitBeforeTravelStepList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_transit_before_travel_step

RouteTransitBeforeTravelStepList: TypeAlias = list[
    "capo_geo_routes.types.route_transit_before_travel_step.RouteTransitBeforeTravelStep"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitBeforeTravelStepList) -> list:
    import capo_geo_routes.types.route_transit_before_travel_step

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.route_transit_before_travel_step.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouteTransitBeforeTravelStepList:
    import capo_geo_routes.types.route_transit_before_travel_step

    out: RouteTransitBeforeTravelStepList = []
    for item in data:
        out.append(
            capo_geo_routes.types.route_transit_before_travel_step.deserialize_json(
                item
            )
        )
    return out
