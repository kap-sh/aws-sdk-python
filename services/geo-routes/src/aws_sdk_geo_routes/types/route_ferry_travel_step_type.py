"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteFerryTravelStepType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteFerryTravelStepType: TypeAlias = Literal[
    "Depart",
    "Continue",
    "Arrive",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Depart",
        "Continue",
        "Arrive",
    )
)


def serialize_json(value: RouteFerryTravelStepType) -> str:
    return value


def deserialize_json(data: str) -> RouteFerryTravelStepType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteFerryTravelStepType value: {data!r}")
    return cast(RouteFerryTravelStepType, data)
