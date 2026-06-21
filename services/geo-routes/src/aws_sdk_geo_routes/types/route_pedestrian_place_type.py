"""Generated from Smithy shape ``com.amazonaws.georoutes#RoutePedestrianPlaceType``."""

from typing import Literal, TypeAlias, cast

RoutePedestrianPlaceType: TypeAlias = Literal[
    "AccessPoint",
    "DockingStation",
    "ParkingLot",
    "Station",
]


# --- restJson1 ser/de ---
def serialize_json(value: RoutePedestrianPlaceType) -> str:
    return value


def deserialize_json(data: str) -> RoutePedestrianPlaceType:
    return cast(RoutePedestrianPlaceType, data)
