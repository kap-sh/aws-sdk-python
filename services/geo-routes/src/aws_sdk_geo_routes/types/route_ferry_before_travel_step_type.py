"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteFerryBeforeTravelStepType``."""

from typing import Literal, TypeAlias, cast

RouteFerryBeforeTravelStepType: TypeAlias = Literal["Board",]


# --- restJson1 ser/de ---
def serialize_json(value: RouteFerryBeforeTravelStepType) -> str:
    return value


def deserialize_json(data: str) -> RouteFerryBeforeTravelStepType:
    return cast(RouteFerryBeforeTravelStepType, data)
