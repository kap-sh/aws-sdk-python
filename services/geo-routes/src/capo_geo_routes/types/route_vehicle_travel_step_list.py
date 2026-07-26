"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleTravelStepList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.route_vehicle_travel_step

RouteVehicleTravelStepList: TypeAlias = list[
    "capo_geo_routes.types.route_vehicle_travel_step.RouteVehicleTravelStep"
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteVehicleTravelStepList) -> list:
    import capo_geo_routes.types.route_vehicle_travel_step

    out: list = []
    for item in value:
        out.append(capo_geo_routes.types.route_vehicle_travel_step.serialize_json(item))
    return out


def deserialize_json(data: list) -> RouteVehicleTravelStepList:
    import capo_geo_routes.types.route_vehicle_travel_step

    out: RouteVehicleTravelStepList = []
    for item in data:
        out.append(
            capo_geo_routes.types.route_vehicle_travel_step.deserialize_json(item)
        )
    return out
