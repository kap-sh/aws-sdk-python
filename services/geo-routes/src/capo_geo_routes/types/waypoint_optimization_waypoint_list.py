"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationWaypointList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_geo_routes.types.waypoint_optimization_waypoint

WaypointOptimizationWaypointList: TypeAlias = list[
    "capo_geo_routes.types.waypoint_optimization_waypoint.WaypointOptimizationWaypoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationWaypointList) -> list:
    import capo_geo_routes.types.waypoint_optimization_waypoint

    out: list = []
    for item in value:
        out.append(
            capo_geo_routes.types.waypoint_optimization_waypoint.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> WaypointOptimizationWaypointList:
    import capo_geo_routes.types.waypoint_optimization_waypoint

    out: WaypointOptimizationWaypointList = []
    for item in data:
        out.append(
            capo_geo_routes.types.waypoint_optimization_waypoint.deserialize_json(item)
        )
    return out
