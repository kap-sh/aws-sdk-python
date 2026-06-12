"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteRentalTravelStepType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteRentalTravelStepType: TypeAlias = Literal[
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


def serialize_json(value: RouteRentalTravelStepType) -> str:
    return value


def deserialize_json(data: str) -> RouteRentalTravelStepType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteRentalTravelStepType value: {data!r}")
    return cast(RouteRentalTravelStepType, data)
