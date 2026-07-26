"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSpanCarAccessAttribute``."""

from typing import Literal, TypeAlias, cast

RouteSpanCarAccessAttribute: TypeAlias = Literal[
    "Allowed",
    "NoThroughTraffic",
    "TollRoad",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteSpanCarAccessAttribute) -> str:
    return value


def deserialize_json(data: str) -> RouteSpanCarAccessAttribute:
    return cast(RouteSpanCarAccessAttribute, data)
