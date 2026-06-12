"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationClusteringAlgorithm``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

WaypointOptimizationClusteringAlgorithm: TypeAlias = Literal[
    "DrivingDistance",
    "TopologySegment",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DrivingDistance",
        "TopologySegment",
    )
)


def serialize_json(value: WaypointOptimizationClusteringAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> WaypointOptimizationClusteringAlgorithm:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown WaypointOptimizationClusteringAlgorithm value: {data!r}"
        )
    return cast(WaypointOptimizationClusteringAlgorithm, data)
