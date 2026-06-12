"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteHazardousCargoType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

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


def serialize_json(value: RouteHazardousCargoType) -> str:
    return value


def deserialize_json(data: str) -> RouteHazardousCargoType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteHazardousCargoType value: {data!r}")
    return cast(RouteHazardousCargoType, data)
