"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationSequencingObjective``."""

from typing import Literal, TypeAlias, cast

WaypointOptimizationSequencingObjective: TypeAlias = Literal[
    "FastestRoute",
    "ShortestRoute",
]


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationSequencingObjective) -> str:
    return value


def deserialize_json(data: str) -> WaypointOptimizationSequencingObjective:
    return cast(WaypointOptimizationSequencingObjective, data)
