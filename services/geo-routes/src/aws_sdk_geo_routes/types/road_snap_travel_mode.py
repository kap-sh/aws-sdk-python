"""Generated from Smithy shape ``com.amazonaws.georoutes#RoadSnapTravelMode``."""

from typing import Literal, TypeAlias, cast

RoadSnapTravelMode: TypeAlias = Literal[
    "Car",
    "Pedestrian",
    "Scooter",
    "Truck",
]


# --- restJson1 ser/de ---
def serialize_json(value: RoadSnapTravelMode) -> str:
    return value


def deserialize_json(data: str) -> RoadSnapTravelMode:
    return cast(RoadSnapTravelMode, data)
