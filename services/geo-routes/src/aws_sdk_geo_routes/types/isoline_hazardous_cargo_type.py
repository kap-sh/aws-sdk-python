"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineHazardousCargoType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

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


def serialize_json(value: IsolineHazardousCargoType) -> str:
    return value


def deserialize_json(data: str) -> IsolineHazardousCargoType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IsolineHazardousCargoType value: {data!r}")
    return cast(IsolineHazardousCargoType, data)
