"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteFerryTravelStepType``."""

from typing import Literal, TypeAlias, cast

RouteFerryTravelStepType: TypeAlias = Literal[
    "Depart",
    "Continue",
    "Arrive",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteFerryTravelStepType) -> str:
    return value


def deserialize_json(data: str) -> RouteFerryTravelStepType:
    return cast(RouteFerryTravelStepType, data)
