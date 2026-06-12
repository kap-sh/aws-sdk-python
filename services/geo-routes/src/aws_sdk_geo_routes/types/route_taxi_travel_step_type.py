"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTaxiTravelStepType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteTaxiTravelStepType: TypeAlias = Literal[
    "Arrive",
    "Continue",
    "Depart",
    "Exit",
    "Keep",
    "Ramp",
    "RoundaboutEnter",
    "RoundaboutExit",
    "RoundaboutPass",
    "Turn",
    "UTurn",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Arrive",
        "Continue",
        "Depart",
        "Exit",
        "Keep",
        "Ramp",
        "RoundaboutEnter",
        "RoundaboutExit",
        "RoundaboutPass",
        "Turn",
        "UTurn",
    )
)


def serialize_json(value: RouteTaxiTravelStepType) -> str:
    return value


def deserialize_json(data: str) -> RouteTaxiTravelStepType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteTaxiTravelStepType value: {data!r}")
    return cast(RouteTaxiTravelStepType, data)
