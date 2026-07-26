"""Generated from Smithy shape ``com.amazonaws.georoutes#RoutePedestrianTravelStepType``."""

from typing import Literal, TypeAlias, cast

RoutePedestrianTravelStepType: TypeAlias = Literal[
    "Arrive",
    "Continue",
    "Depart",
    "Keep",
    "RoundaboutEnter",
    "RoundaboutExit",
    "RoundaboutPass",
    "Turn",
]


# --- restJson1 ser/de ---
def serialize_json(value: RoutePedestrianTravelStepType) -> str:
    return value


def deserialize_json(data: str) -> RoutePedestrianTravelStepType:
    return cast(RoutePedestrianTravelStepType, data)
