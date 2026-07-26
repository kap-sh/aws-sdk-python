"""Generated from Smithy shape ``com.amazonaws.georoutes#RoadSnapHazardousCargoType``."""

from typing import Literal, TypeAlias, cast

RoadSnapHazardousCargoType: TypeAlias = Literal[
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
def serialize_json(value: RoadSnapHazardousCargoType) -> str:
    return value


def deserialize_json(data: str) -> RoadSnapHazardousCargoType:
    return cast(RoadSnapHazardousCargoType, data)
