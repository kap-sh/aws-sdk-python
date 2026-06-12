"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixZoneCategory``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteMatrixZoneCategory: TypeAlias = Literal[
    "CongestionPricing",
    "Environmental",
    "Vignette",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CongestionPricing",
        "Environmental",
        "Vignette",
    )
)


def serialize_json(value: RouteMatrixZoneCategory) -> str:
    return value


def deserialize_json(data: str) -> RouteMatrixZoneCategory:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteMatrixZoneCategory value: {data!r}")
    return cast(RouteMatrixZoneCategory, data)
