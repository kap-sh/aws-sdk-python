"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationTravelMode``."""

from typing import Literal, TypeAlias, cast

WaypointOptimizationTravelMode: TypeAlias = Literal[
    "Car",
    "Pedestrian",
    "Scooter",
    "Truck",
]


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationTravelMode) -> str:
    return value


def deserialize_json(data: str) -> WaypointOptimizationTravelMode:
    return cast(WaypointOptimizationTravelMode, data)
