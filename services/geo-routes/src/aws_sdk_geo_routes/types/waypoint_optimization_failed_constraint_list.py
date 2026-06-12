"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationFailedConstraintList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.waypoint_optimization_failed_constraint

WaypointOptimizationFailedConstraintList: TypeAlias = list[
    "aws_sdk_geo_routes.types.waypoint_optimization_failed_constraint.WaypointOptimizationFailedConstraint"
]


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationFailedConstraintList) -> list:
    import aws_sdk_geo_routes.types.waypoint_optimization_failed_constraint

    out: list = []
    for item in value:
        out.append(
            aws_sdk_geo_routes.types.waypoint_optimization_failed_constraint.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> WaypointOptimizationFailedConstraintList:
    import aws_sdk_geo_routes.types.waypoint_optimization_failed_constraint

    out: WaypointOptimizationFailedConstraintList = []
    for item in data:
        out.append(
            aws_sdk_geo_routes.types.waypoint_optimization_failed_constraint.deserialize_json(
                item
            )
        )
    return out
