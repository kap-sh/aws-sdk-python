"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteZoneCategory``."""

from typing import Literal, TypeAlias, cast

RouteZoneCategory: TypeAlias = Literal[
    "CongestionPricing",
    "Environmental",
    "Vignette",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteZoneCategory) -> str:
    return value


def deserialize_json(data: str) -> RouteZoneCategory:
    return cast(RouteZoneCategory, data)
