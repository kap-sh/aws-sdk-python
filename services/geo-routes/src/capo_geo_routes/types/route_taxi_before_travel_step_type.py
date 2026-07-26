"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTaxiBeforeTravelStepType``."""

from typing import Literal, TypeAlias, cast

RouteTaxiBeforeTravelStepType: TypeAlias = Literal["Wait",]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTaxiBeforeTravelStepType) -> str:
    return value


def deserialize_json(data: str) -> RouteTaxiBeforeTravelStepType:
    return cast(RouteTaxiBeforeTravelStepType, data)
