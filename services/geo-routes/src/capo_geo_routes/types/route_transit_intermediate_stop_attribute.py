"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitIntermediateStopAttribute``."""

from typing import Literal, TypeAlias, cast

RouteTransitIntermediateStopAttribute: TypeAlias = Literal[
    "NoEntry",
    "NoExit",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitIntermediateStopAttribute) -> str:
    return value


def deserialize_json(data: str) -> RouteTransitIntermediateStopAttribute:
    return cast(RouteTransitIntermediateStopAttribute, data)
