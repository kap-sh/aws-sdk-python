"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTaxiPlaceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteTaxiPlaceType: TypeAlias = Literal[
    "AccessPoint",
    "Station",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AccessPoint",
        "Station",
    )
)


def serialize_json(value: RouteTaxiPlaceType) -> str:
    return value


def deserialize_json(data: str) -> RouteTaxiPlaceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteTaxiPlaceType value: {data!r}")
    return cast(RouteTaxiPlaceType, data)
