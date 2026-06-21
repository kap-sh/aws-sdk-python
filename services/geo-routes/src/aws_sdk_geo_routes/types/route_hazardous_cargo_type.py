"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteHazardousCargoType``."""

from typing import Literal, TypeAlias, cast

RouteHazardousCargoType: TypeAlias = Literal[
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
def serialize_json(value: RouteHazardousCargoType) -> str:
    return value


def deserialize_json(data: str) -> RouteHazardousCargoType:
    return cast(RouteHazardousCargoType, data)
