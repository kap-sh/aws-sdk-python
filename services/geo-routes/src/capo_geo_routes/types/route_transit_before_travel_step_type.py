"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitBeforeTravelStepType``."""

from typing import Literal, TypeAlias, cast

RouteTransitBeforeTravelStepType: TypeAlias = Literal["Board",]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitBeforeTravelStepType) -> str:
    return value


def deserialize_json(data: str) -> RouteTransitBeforeTravelStepType:
    return cast(RouteTransitBeforeTravelStepType, data)
