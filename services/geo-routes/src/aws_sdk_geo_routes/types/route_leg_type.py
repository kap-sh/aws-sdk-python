"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteLegType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteLegType: TypeAlias = Literal[
    "Ferry",
    "Pedestrian",
    "Vehicle",
    "Rental",
    "Taxi",
    "Transit",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Ferry",
        "Pedestrian",
        "Vehicle",
        "Rental",
        "Taxi",
        "Transit",
    )
)


def serialize_json(value: RouteLegType) -> str:
    return value


def deserialize_json(data: str) -> RouteLegType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteLegType value: {data!r}")
    return cast(RouteLegType, data)
