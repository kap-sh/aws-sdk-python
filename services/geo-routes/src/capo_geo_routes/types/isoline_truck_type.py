"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineTruckType``."""

from typing import Literal, TypeAlias, cast

IsolineTruckType: TypeAlias = Literal[
    "LightTruck",
    "StraightTruck",
    "Tractor",
]


# --- restJson1 ser/de ---
def serialize_json(value: IsolineTruckType) -> str:
    return value


def deserialize_json(data: str) -> IsolineTruckType:
    return cast(IsolineTruckType, data)
