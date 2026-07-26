"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleAfterTravelStepList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_vehicle_after_travel_step

RouteVehicleAfterTravelStepList: TypeAlias = list[
    "capo_geo_routes.types.route_vehicle_after_travel_step.RouteVehicleAfterTravelStep"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteVehicleAfterTravelStepList) -> list:
    import capo_geo_routes.types.route_vehicle_after_travel_step

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.route_vehicle_after_travel_step.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RouteVehicleAfterTravelStepList:
    import capo_geo_routes.types.route_vehicle_after_travel_step

    out: RouteVehicleAfterTravelStepList = []
    for item in data:
        out.append(
            capo_geo_routes.types.route_vehicle_after_travel_step.deserialize_json(item)
        )
    return out
