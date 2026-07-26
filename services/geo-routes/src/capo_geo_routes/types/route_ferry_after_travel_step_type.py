"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteFerryAfterTravelStepType``."""

from typing import Literal, TypeAlias, cast

RouteFerryAfterTravelStepType: TypeAlias = Literal["Deboard",]


# --- restJson1 ser/de ---
def serialize_json(value: RouteFerryAfterTravelStepType) -> str:
    return value


def deserialize_json(data: str) -> RouteFerryAfterTravelStepType:
    return cast(RouteFerryAfterTravelStepType, data)
