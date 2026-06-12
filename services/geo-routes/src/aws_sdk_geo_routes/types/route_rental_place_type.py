"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteRentalPlaceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteRentalPlaceType: TypeAlias = Literal[
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


def serialize_json(value: RouteRentalPlaceType) -> str:
    return value


def deserialize_json(data: str) -> RouteRentalPlaceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteRentalPlaceType value: {data!r}")
    return cast(RouteRentalPlaceType, data)
