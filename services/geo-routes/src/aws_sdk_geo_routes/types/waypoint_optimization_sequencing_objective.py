"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationSequencingObjective``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

WaypointOptimizationSequencingObjective: TypeAlias = Literal[
    "FastestRoute",
    "ShortestRoute",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FastestRoute",
        "ShortestRoute",
    )
)


def serialize_json(value: WaypointOptimizationSequencingObjective) -> str:
    return value


def deserialize_json(data: str) -> WaypointOptimizationSequencingObjective:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown WaypointOptimizationSequencingObjective value: {data!r}"
        )
    return cast(WaypointOptimizationSequencingObjective, data)
