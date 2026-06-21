"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTaxiAfterTravelStepType``."""

from typing import Literal, TypeAlias, cast

RouteTaxiAfterTravelStepType: TypeAlias = Literal["Park",]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTaxiAfterTravelStepType) -> str:
    return value


def deserialize_json(data: str) -> RouteTaxiAfterTravelStepType:
    return cast(RouteTaxiAfterTravelStepType, data)
