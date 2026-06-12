"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationHazardousCargoTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.waypoint_optimization_hazardous_cargo_type

WaypointOptimizationHazardousCargoTypeList: TypeAlias = list[
    "aws_sdk_geo_routes.types.waypoint_optimization_hazardous_cargo_type.WaypointOptimizationHazardousCargoType"
]


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationHazardousCargoTypeList) -> list:
    import aws_sdk_geo_routes.types.waypoint_optimization_hazardous_cargo_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_geo_routes.types.waypoint_optimization_hazardous_cargo_type.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> WaypointOptimizationHazardousCargoTypeList:
    import aws_sdk_geo_routes.types.waypoint_optimization_hazardous_cargo_type

    out: WaypointOptimizationHazardousCargoTypeList = []
    for item in data:
        out.append(
            aws_sdk_geo_routes.types.waypoint_optimization_hazardous_cargo_type.deserialize_json(
                item
            )
        )
    return out
