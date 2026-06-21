"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteAccessibilityAvailability``."""

from typing import Literal, TypeAlias, cast

RouteAccessibilityAvailability: TypeAlias = Literal[
    "Available",
    "Limited",
    "Unavailable",
    "Unknown",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteAccessibilityAvailability) -> str:
    return value


def deserialize_json(data: str) -> RouteAccessibilityAvailability:
    return cast(RouteAccessibilityAvailability, data)
