"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitTripStatus``."""

from typing import Literal, TypeAlias, cast

RouteTransitTripStatus: TypeAlias = Literal[
    "Added",
    "Cancelled",
    "Replaced",
    "Scheduled",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitTripStatus) -> str:
    return value


def deserialize_json(data: str) -> RouteTransitTripStatus:
    return cast(RouteTransitTripStatus, data)
