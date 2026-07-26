"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSpanScooterAccessAttribute``."""

from typing import Literal, TypeAlias, cast

RouteSpanScooterAccessAttribute: TypeAlias = Literal[
    "Allowed",
    "NoThroughTraffic",
    "TollRoad",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteSpanScooterAccessAttribute) -> str:
    return value


def deserialize_json(data: str) -> RouteSpanScooterAccessAttribute:
    return cast(RouteSpanScooterAccessAttribute, data)
