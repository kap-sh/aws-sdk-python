"""Generated from Smithy shape ``com.amazonaws.georoutes#RoutingObjective``."""

from typing import Literal, TypeAlias, cast

RoutingObjective: TypeAlias = Literal[
    "FastestRoute",
    "ShortestRoute",
]


# --- restJson1 ser/de ---
def serialize_json(value: RoutingObjective) -> str:
    return value


def deserialize_json(data: str) -> RoutingObjective:
    return cast(RoutingObjective, data)
