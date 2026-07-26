"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTaxiBeforeTravelStepList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_taxi_before_travel_step

RouteTaxiBeforeTravelStepList: TypeAlias = list[
    "capo_geo_routes.types.route_taxi_before_travel_step.RouteTaxiBeforeTravelStep"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTaxiBeforeTravelStepList) -> list:
    import capo_geo_routes.types.route_taxi_before_travel_step

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.route_taxi_before_travel_step.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouteTaxiBeforeTravelStepList:
    import capo_geo_routes.types.route_taxi_before_travel_step

    out: RouteTaxiBeforeTravelStepList = []
    for item in data:
        out.append(
            capo_geo_routes.types.route_taxi_before_travel_step.deserialize_json(item)
        )
    return out
