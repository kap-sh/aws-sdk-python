"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteLegType``."""

from typing import Literal, TypeAlias, cast

RouteLegType: TypeAlias = Literal[
    "Ferry",
    "Pedestrian",
    "Vehicle",
    "Rental",
    "Taxi",
    "Transit",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteLegType) -> str:
    return value


def deserialize_json(data: str) -> RouteLegType:
    return cast(RouteLegType, data)
