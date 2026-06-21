"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteRentalAfterTravelStepType``."""

from typing import Literal, TypeAlias, cast

RouteRentalAfterTravelStepType: TypeAlias = Literal["Park",]


# --- restJson1 ser/de ---
def serialize_json(value: RouteRentalAfterTravelStepType) -> str:
    return value


def deserialize_json(data: str) -> RouteRentalAfterTravelStepType:
    return cast(RouteRentalAfterTravelStepType, data)
