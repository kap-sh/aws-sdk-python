"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationTruckType``."""

from typing import Literal, TypeAlias, cast

WaypointOptimizationTruckType: TypeAlias = Literal[
    "StraightTruck",
    "Tractor",
]


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationTruckType) -> str:
    return value


def deserialize_json(data: str) -> WaypointOptimizationTruckType:
    return cast(WaypointOptimizationTruckType, data)
