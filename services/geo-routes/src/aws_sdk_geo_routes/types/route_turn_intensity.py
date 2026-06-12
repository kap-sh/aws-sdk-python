"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTurnIntensity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteTurnIntensity: TypeAlias = Literal[
    "Sharp",
    "Slight",
    "Typical",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Sharp",
        "Slight",
        "Typical",
    )
)


def serialize_json(value: RouteTurnIntensity) -> str:
    return value


def deserialize_json(data: str) -> RouteTurnIntensity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteTurnIntensity value: {data!r}")
    return cast(RouteTurnIntensity, data)
