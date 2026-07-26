"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationAvoidanceAreaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.waypoint_optimization_avoidance_area

WaypointOptimizationAvoidanceAreaList: TypeAlias = list[
    "capo_geo_routes.types.waypoint_optimization_avoidance_area.WaypointOptimizationAvoidanceArea"
]


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationAvoidanceAreaList) -> list:
    import capo_geo_routes.types.waypoint_optimization_avoidance_area

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.waypoint_optimization_avoidance_area.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> WaypointOptimizationAvoidanceAreaList:
    import capo_geo_routes.types.waypoint_optimization_avoidance_area

    out: WaypointOptimizationAvoidanceAreaList = []
    for item in data:
        out.append(
            capo_geo_routes.types.waypoint_optimization_avoidance_area.deserialize_json(
                item
            )
        )
    return out
