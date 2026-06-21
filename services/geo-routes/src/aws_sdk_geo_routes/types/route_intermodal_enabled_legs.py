"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteIntermodalEnabledLegs``."""

from typing import Literal, TypeAlias, cast

RouteIntermodalEnabledLegs: TypeAlias = Literal[
    "FirstLeg",
    "LastLeg",
    "EntireRoute",
    "None",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteIntermodalEnabledLegs) -> str:
    return value


def deserialize_json(data: str) -> RouteIntermodalEnabledLegs:
    return cast(RouteIntermodalEnabledLegs, data)
