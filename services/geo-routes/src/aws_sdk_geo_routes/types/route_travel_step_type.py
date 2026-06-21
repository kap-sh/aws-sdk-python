"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTravelStepType``."""

from typing import Literal, TypeAlias, cast

RouteTravelStepType: TypeAlias = Literal[
    "Default",
    "TurnByTurn",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTravelStepType) -> str:
    return value


def deserialize_json(data: str) -> RouteTravelStepType:
    return cast(RouteTravelStepType, data)
