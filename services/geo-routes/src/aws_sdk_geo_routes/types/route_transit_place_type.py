"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitPlaceType``."""

from typing import Literal, TypeAlias, cast

RouteTransitPlaceType: TypeAlias = Literal["Station",]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitPlaceType) -> str:
    return value


def deserialize_json(data: str) -> RouteTransitPlaceType:
    return cast(RouteTransitPlaceType, data)
