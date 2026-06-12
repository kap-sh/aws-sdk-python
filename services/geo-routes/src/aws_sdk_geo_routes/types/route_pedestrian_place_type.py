"""Generated from Smithy shape ``com.amazonaws.georoutes#RoutePedestrianPlaceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RoutePedestrianPlaceType: TypeAlias = Literal[
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


def serialize_json(value: RoutePedestrianPlaceType) -> str:
    return value


def deserialize_json(data: str) -> RoutePedestrianPlaceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RoutePedestrianPlaceType value: {data!r}")
    return cast(RoutePedestrianPlaceType, data)
