"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteRentalBeforeTravelStepType``."""

from typing import Literal, TypeAlias, cast

RouteRentalBeforeTravelStepType: TypeAlias = Literal["Setup",]


# --- restJson1 ser/de ---
def serialize_json(value: RouteRentalBeforeTravelStepType) -> str:
    return value


def deserialize_json(data: str) -> RouteRentalBeforeTravelStepType:
    return cast(RouteRentalBeforeTravelStepType, data)
