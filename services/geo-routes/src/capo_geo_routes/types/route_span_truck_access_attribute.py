"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteSpanTruckAccessAttribute``."""

from typing import Literal, TypeAlias, cast

RouteSpanTruckAccessAttribute: TypeAlias = Literal[
    "Allowed",
    "NoThroughTraffic",
    "TollRoad",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteSpanTruckAccessAttribute) -> str:
    return value


def deserialize_json(data: str) -> RouteSpanTruckAccessAttribute:
    return cast(RouteSpanTruckAccessAttribute, data)
