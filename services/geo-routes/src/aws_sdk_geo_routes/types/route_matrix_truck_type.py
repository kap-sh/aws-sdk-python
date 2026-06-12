"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixTruckType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteMatrixTruckType: TypeAlias = Literal[
    "LightTruck",
    "StraightTruck",
    "Tractor",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LightTruck",
        "StraightTruck",
        "Tractor",
    )
)


def serialize_json(value: RouteMatrixTruckType) -> str:
    return value


def deserialize_json(data: str) -> RouteMatrixTruckType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteMatrixTruckType value: {data!r}")
    return cast(RouteMatrixTruckType, data)
