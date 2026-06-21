"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleTravelStepType``."""

from typing import Literal, TypeAlias, cast

RouteVehicleTravelStepType: TypeAlias = Literal[
    "Arrive",
    "Continue",
    "ContinueHighway",
    "Depart",
    "EnterHighway",
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
def serialize_json(value: RouteVehicleTravelStepType) -> str:
    return value


def deserialize_json(data: str) -> RouteVehicleTravelStepType:
    return cast(RouteVehicleTravelStepType, data)
