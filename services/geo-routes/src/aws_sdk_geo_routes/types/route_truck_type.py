"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTruckType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteTruckType: TypeAlias = Literal[
    "LightTruck",
    "StraightTruck",
    "Tractor",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LightTruck",
        "StraightTruck",
        "Tractor",
    )
)


def serialize_json(value: RouteTruckType) -> str:
    return value


def deserialize_json(data: str) -> RouteTruckType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteTruckType value: {data!r}")
    return cast(RouteTruckType, data)
