"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationHazardousCargoType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

WaypointOptimizationHazardousCargoType: TypeAlias = Literal[
    "Combustible",
    "Corrosive",
    "Explosive",
    "Flammable",
    "Gas",
    "HarmfulToWater",
    "Organic",
    "Other",
    "Poison",
    "PoisonousInhalation",
    "Radioactive",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Combustible",
        "Corrosive",
        "Explosive",
        "Flammable",
        "Gas",
        "HarmfulToWater",
        "Organic",
        "Other",
        "Poison",
        "PoisonousInhalation",
        "Radioactive",
    )
)


def serialize_json(value: WaypointOptimizationHazardousCargoType) -> str:
    return value


def deserialize_json(data: str) -> WaypointOptimizationHazardousCargoType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown WaypointOptimizationHazardousCargoType value: {data!r}"
        )
    return cast(WaypointOptimizationHazardousCargoType, data)
