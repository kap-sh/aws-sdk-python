"""Generated from Smithy shape ``com.amazonaws.georoutes#RoutePedestrianAfterTravelStepType``."""

from typing import Literal, TypeAlias, cast

RoutePedestrianAfterTravelStepType: TypeAlias = Literal["Wait",]


# --- restJson1 ser/de ---
def serialize_json(value: RoutePedestrianAfterTravelStepType) -> str:
    return value


def deserialize_json(data: str) -> RoutePedestrianAfterTravelStepType:
    return cast(RoutePedestrianAfterTravelStepType, data)
