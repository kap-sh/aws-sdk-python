"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteRentalMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteRentalMode: TypeAlias = Literal[
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


def serialize_json(value: RouteRentalMode) -> str:
    return value


def deserialize_json(data: str) -> RouteRentalMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteRentalMode value: {data!r}")
    return cast(RouteRentalMode, data)
