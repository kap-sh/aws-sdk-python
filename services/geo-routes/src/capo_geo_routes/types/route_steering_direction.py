"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSteeringDirection``."""

from typing import Literal, TypeAlias, cast

RouteSteeringDirection: TypeAlias = Literal[
    "Left",
    "Right",
    "Straight",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteSteeringDirection) -> str:
    return value


def deserialize_json(data: str) -> RouteSteeringDirection:
    return cast(RouteSteeringDirection, data)
