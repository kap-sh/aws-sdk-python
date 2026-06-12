"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTravelMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteTravelMode: TypeAlias = Literal[
    "Car",
    "Pedestrian",
    "Scooter",
    "Truck",
    "Intermodal",
    "Transit",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Car",
        "Pedestrian",
        "Scooter",
        "Truck",
        "Intermodal",
        "Transit",
    )
)


def serialize_json(value: RouteTravelMode) -> str:
    return value


def deserialize_json(data: str) -> RouteTravelMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteTravelMode value: {data!r}")
    return cast(RouteTravelMode, data)
