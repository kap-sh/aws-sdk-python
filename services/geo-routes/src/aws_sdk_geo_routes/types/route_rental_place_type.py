"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteRentalPlaceType``."""

from typing import Literal, TypeAlias, cast

RouteRentalPlaceType: TypeAlias = Literal[
    "AccessPoint",
    "DockingStation",
    "ParkingLot",
    "Station",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteRentalPlaceType) -> str:
    return value


def deserialize_json(data: str) -> RouteRentalPlaceType:
    return cast(RouteRentalPlaceType, data)
