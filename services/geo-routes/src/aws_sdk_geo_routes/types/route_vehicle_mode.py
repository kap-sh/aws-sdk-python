"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteVehicleMode: TypeAlias = Literal[
    "All",
    "Car",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "All",
        "Car",
    )
)


def serialize_json(value: RouteVehicleMode) -> str:
    return value


def deserialize_json(data: str) -> RouteVehicleMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteVehicleMode value: {data!r}")
    return cast(RouteVehicleMode, data)
