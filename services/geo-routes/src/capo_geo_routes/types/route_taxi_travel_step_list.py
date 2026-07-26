"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTaxiTravelStepList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_taxi_travel_step

RouteTaxiTravelStepList: TypeAlias = list[
    "capo_geo_routes.types.route_taxi_travel_step.RouteTaxiTravelStep"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTaxiTravelStepList) -> list:
    import capo_geo_routes.types.route_taxi_travel_step

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.route_taxi_travel_step.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteTaxiTravelStepList:
    import capo_geo_routes.types.route_taxi_travel_step

    out: RouteTaxiTravelStepList = []
    for item in data:
        out.append(capo_geo_routes.types.route_taxi_travel_step.deserialize_json(item))
    return out
