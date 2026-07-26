"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTravelMode``."""

from typing import Literal, TypeAlias, cast

RouteTravelMode: TypeAlias = Literal[
    "Car",
    "Pedestrian",
    "Scooter",
    "Truck",
    "Intermodal",
    "Transit",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTravelMode) -> str:
    return value


def deserialize_json(data: str) -> RouteTravelMode:
    return cast(RouteTravelMode, data)
