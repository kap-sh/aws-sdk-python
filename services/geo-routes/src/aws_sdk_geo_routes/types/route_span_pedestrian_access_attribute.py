"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSpanPedestrianAccessAttribute``."""

from typing import Literal, TypeAlias, cast

RouteSpanPedestrianAccessAttribute: TypeAlias = Literal[
    "Allowed",
    "Indoors",
    "NoThroughTraffic",
    "Park",
    "Stairs",
    "TollRoad",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteSpanPedestrianAccessAttribute) -> str:
    return value


def deserialize_json(data: str) -> RouteSpanPedestrianAccessAttribute:
    return cast(RouteSpanPedestrianAccessAttribute, data)
