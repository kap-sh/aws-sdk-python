"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehiclePlaceType``."""

from typing import Literal, TypeAlias, cast

RouteVehiclePlaceType: TypeAlias = Literal[
    "AccessPoint",
    "DockingStation",
    "ParkingLot",
    "Station",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteVehiclePlaceType) -> str:
    return value


def deserialize_json(data: str) -> RouteVehiclePlaceType:
    return cast(RouteVehiclePlaceType, data)
