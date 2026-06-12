"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixTravelMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteMatrixTravelMode: TypeAlias = Literal[
    "Car",
    "Pedestrian",
    "Scooter",
    "Truck",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Car",
        "Pedestrian",
        "Scooter",
        "Truck",
    )
)


def serialize_json(value: RouteMatrixTravelMode) -> str:
    return value


def deserialize_json(data: str) -> RouteMatrixTravelMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteMatrixTravelMode value: {data!r}")
    return cast(RouteMatrixTravelMode, data)
