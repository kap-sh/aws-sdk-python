"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTruckType``."""

from typing import Literal, TypeAlias, cast

RouteTruckType: TypeAlias = Literal[
    "LightTruck",
    "StraightTruck",
    "Tractor",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTruckType) -> str:
    return value


def deserialize_json(data: str) -> RouteTruckType:
    return cast(RouteTruckType, data)
