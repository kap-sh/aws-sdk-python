"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehiclePlaceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteVehiclePlaceType: TypeAlias = Literal[
    "AccessPoint",
    "DockingStation",
    "ParkingLot",
    "Station",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AccessPoint",
        "DockingStation",
        "ParkingLot",
        "Station",
    )
)


def serialize_json(value: RouteVehiclePlaceType) -> str:
    return value


def deserialize_json(data: str) -> RouteVehiclePlaceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteVehiclePlaceType value: {data!r}")
    return cast(RouteVehiclePlaceType, data)
