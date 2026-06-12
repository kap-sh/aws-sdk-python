"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationTravelMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

WaypointOptimizationTravelMode: TypeAlias = Literal[
    "Car",
    "Pedestrian",
    "Scooter",
    "Truck",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Car",
        "Pedestrian",
        "Scooter",
        "Truck",
    )
)


def serialize_json(value: WaypointOptimizationTravelMode) -> str:
    return value


def deserialize_json(data: str) -> WaypointOptimizationTravelMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown WaypointOptimizationTravelMode value: {data!r}"
        )
    return cast(WaypointOptimizationTravelMode, data)
