"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleAfterTravelStepType``."""

from typing import Literal, TypeAlias, cast

RouteVehicleAfterTravelStepType: TypeAlias = Literal["Park",]


# --- restJson1 ser/de ---
def serialize_json(value: RouteVehicleAfterTravelStepType) -> str:
    return value


def deserialize_json(data: str) -> RouteVehicleAfterTravelStepType:
    return cast(RouteVehicleAfterTravelStepType, data)
