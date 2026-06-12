"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteZoneCategory``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteZoneCategory: TypeAlias = Literal[
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


def serialize_json(value: RouteZoneCategory) -> str:
    return value


def deserialize_json(data: str) -> RouteZoneCategory:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteZoneCategory value: {data!r}")
    return cast(RouteZoneCategory, data)
