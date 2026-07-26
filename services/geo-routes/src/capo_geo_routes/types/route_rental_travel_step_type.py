"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteRentalTravelStepType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: RouteRentalTravelStepType) -> str:
    return value


def deserialize_json(data: str) -> RouteRentalTravelStepType:
    return cast(RouteRentalTravelStepType, data)
