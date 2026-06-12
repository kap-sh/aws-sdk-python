"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationOptimizedWaypointList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.waypoint_optimization_optimized_waypoint

WaypointOptimizationOptimizedWaypointList: TypeAlias = list[
    "aws_sdk_geo_routes.types.waypoint_optimization_optimized_waypoint.WaypointOptimizationOptimizedWaypoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationOptimizedWaypointList) -> list:
    import aws_sdk_geo_routes.types.waypoint_optimization_optimized_waypoint

    out: list = []
    for item in value:
        out.append(
            aws_sdk_geo_routes.types.waypoint_optimization_optimized_waypoint.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> WaypointOptimizationOptimizedWaypointList:
    import aws_sdk_geo_routes.types.waypoint_optimization_optimized_waypoint

    out: WaypointOptimizationOptimizedWaypointList = []
    for item in data:
        out.append(
            aws_sdk_geo_routes.types.waypoint_optimization_optimized_waypoint.deserialize_json(
                item
            )
        )
    return out
