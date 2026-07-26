"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitAfterTravelStepType``."""

from typing import Literal, TypeAlias, cast

RouteTransitAfterTravelStepType: TypeAlias = Literal["Deboard",]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitAfterTravelStepType) -> str:
    return value


def deserialize_json(data: str) -> RouteTransitAfterTravelStepType:
    return cast(RouteTransitAfterTravelStepType, data)
