"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTaxiTravelStepType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: RouteTaxiTravelStepType) -> str:
    return value


def deserialize_json(data: str) -> RouteTaxiTravelStepType:
    return cast(RouteTaxiTravelStepType, data)
