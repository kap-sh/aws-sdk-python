"""Generated from Smithy shape ``com.amazonaws.georoutes#RoadSnapHazardousCargoType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

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


def serialize_json(value: RoadSnapHazardousCargoType) -> str:
    return value


def deserialize_json(data: str) -> RoadSnapHazardousCargoType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RoadSnapHazardousCargoType value: {data!r}"
        )
    return cast(RoadSnapHazardousCargoType, data)
