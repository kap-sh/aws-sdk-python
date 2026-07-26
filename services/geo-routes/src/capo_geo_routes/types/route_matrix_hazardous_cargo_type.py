"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixHazardousCargoType``."""

from typing import Literal, TypeAlias, cast

RouteMatrixHazardousCargoType: TypeAlias = Literal[
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
def serialize_json(value: RouteMatrixHazardousCargoType) -> str:
    return value


def deserialize_json(data: str) -> RouteMatrixHazardousCargoType:
    return cast(RouteMatrixHazardousCargoType, data)
