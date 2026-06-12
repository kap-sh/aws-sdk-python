"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationTruckType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

WaypointOptimizationTruckType: TypeAlias = Literal[
    "StraightTruck",
    "Tractor",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "StraightTruck",
        "Tractor",
    )
)


def serialize_json(value: WaypointOptimizationTruckType) -> str:
    return value


def deserialize_json(data: str) -> WaypointOptimizationTruckType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown WaypointOptimizationTruckType value: {data!r}"
        )
    return cast(WaypointOptimizationTruckType, data)
