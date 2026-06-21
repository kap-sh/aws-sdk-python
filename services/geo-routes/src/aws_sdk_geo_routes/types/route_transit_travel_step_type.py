"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitTravelStepType``."""

from typing import Literal, TypeAlias, cast

RouteTransitTravelStepType: TypeAlias = Literal["Depart",]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitTravelStepType) -> str:
    return value


def deserialize_json(data: str) -> RouteTransitTravelStepType:
    return cast(RouteTransitTravelStepType, data)
