"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationImpedingWaypointList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.waypoint_optimization_impeding_waypoint

WaypointOptimizationImpedingWaypointList: TypeAlias = list[
    "aws_sdk_geo_routes.types.waypoint_optimization_impeding_waypoint.WaypointOptimizationImpedingWaypoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationImpedingWaypointList) -> list:
    import aws_sdk_geo_routes.types.waypoint_optimization_impeding_waypoint

    out: list = []
    for item in value:
        out.append(
            aws_sdk_geo_routes.types.waypoint_optimization_impeding_waypoint.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> WaypointOptimizationImpedingWaypointList:
    import aws_sdk_geo_routes.types.waypoint_optimization_impeding_waypoint

    out: WaypointOptimizationImpedingWaypointList = []
    for item in data:
        out.append(
            aws_sdk_geo_routes.types.waypoint_optimization_impeding_waypoint.deserialize_json(
                item
            )
        )
    return out
