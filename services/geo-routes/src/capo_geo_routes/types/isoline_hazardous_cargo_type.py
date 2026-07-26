"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineHazardousCargoType``."""

from typing import Literal, TypeAlias, cast

IsolineHazardousCargoType: TypeAlias = Literal[
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
def serialize_json(value: IsolineHazardousCargoType) -> str:
    return value


def deserialize_json(data: str) -> IsolineHazardousCargoType:
    return cast(IsolineHazardousCargoType, data)
