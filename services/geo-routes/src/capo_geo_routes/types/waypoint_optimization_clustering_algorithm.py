"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationClusteringAlgorithm``."""

from typing import Literal, TypeAlias, cast

WaypointOptimizationClusteringAlgorithm: TypeAlias = Literal[
    "DrivingDistance",
    "TopologySegment",
]


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationClusteringAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> WaypointOptimizationClusteringAlgorithm:
    return cast(WaypointOptimizationClusteringAlgorithm, data)
