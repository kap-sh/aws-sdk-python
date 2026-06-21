"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationHazardousCargoType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: WaypointOptimizationHazardousCargoType) -> str:
    return value


def deserialize_json(data: str) -> WaypointOptimizationHazardousCargoType:
    return cast(WaypointOptimizationHazardousCargoType, data)
