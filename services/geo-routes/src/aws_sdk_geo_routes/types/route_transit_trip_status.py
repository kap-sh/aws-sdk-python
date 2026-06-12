"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitTripStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteTransitTripStatus: TypeAlias = Literal[
    "Added",
    "Cancelled",
    "Replaced",
    "Scheduled",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Added",
        "Cancelled",
        "Replaced",
        "Scheduled",
    )
)


def serialize_json(value: RouteTransitTripStatus) -> str:
    return value


def deserialize_json(data: str) -> RouteTransitTripStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteTransitTripStatus value: {data!r}")
    return cast(RouteTransitTripStatus, data)
