"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineTravelMode``."""

from typing import Literal, TypeAlias, cast

IsolineTravelMode: TypeAlias = Literal[
    "Car",
    "Pedestrian",
    "Scooter",
    "Truck",
]


# --- restJson1 ser/de ---
def serialize_json(value: IsolineTravelMode) -> str:
    return value


def deserialize_json(data: str) -> IsolineTravelMode:
    return cast(IsolineTravelMode, data)
