"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteAccessibilityAvailability``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteAccessibilityAvailability: TypeAlias = Literal[
    "Available",
    "Limited",
    "Unavailable",
    "Unknown",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Available",
        "Limited",
        "Unavailable",
        "Unknown",
    )
)


def serialize_json(value: RouteAccessibilityAvailability) -> str:
    return value


def deserialize_json(data: str) -> RouteAccessibilityAvailability:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RouteAccessibilityAvailability value: {data!r}"
        )
    return cast(RouteAccessibilityAvailability, data)
