"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteDirection``."""

from typing import Literal, TypeAlias, cast

RouteDirection: TypeAlias = Literal[
    "East",
    "North",
    "South",
    "West",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteDirection) -> str:
    return value


def deserialize_json(data: str) -> RouteDirection:
    return cast(RouteDirection, data)
