"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineTruckType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

IsolineTruckType: TypeAlias = Literal[
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


def serialize_json(value: IsolineTruckType) -> str:
    return value


def deserialize_json(data: str) -> IsolineTruckType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IsolineTruckType value: {data!r}")
    return cast(IsolineTruckType, data)
