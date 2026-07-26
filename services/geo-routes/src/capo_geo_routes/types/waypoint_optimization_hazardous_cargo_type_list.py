"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationHazardousCargoTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.waypoint_optimization_hazardous_cargo_type

WaypointOptimizationHazardousCargoTypeList: TypeAlias = list[
    "capo_geo_routes.types.waypoint_optimization_hazardous_cargo_type.WaypointOptimizationHazardousCargoType"
]


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationHazardousCargoTypeList) -> list:
    import capo_geo_routes.types.waypoint_optimization_hazardous_cargo_type

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.waypoint_optimization_hazardous_cargo_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> WaypointOptimizationHazardousCargoTypeList:
    import capo_geo_routes.types.waypoint_optimization_hazardous_cargo_type

    out: WaypointOptimizationHazardousCargoTypeList = []
    for item in data:
        out.append(
            capo_geo_routes.types.waypoint_optimization_hazardous_cargo_type.deserialize_json(
                item
            )
        )
    return out
