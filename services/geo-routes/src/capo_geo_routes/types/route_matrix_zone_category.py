"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixZoneCategory``."""

from typing import Literal, TypeAlias, cast

RouteMatrixZoneCategory: TypeAlias = Literal[
    "CongestionPricing",
    "Environmental",
    "Vignette",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixZoneCategory) -> str:
    return value


def deserialize_json(data: str) -> RouteMatrixZoneCategory:
    return cast(RouteMatrixZoneCategory, data)
