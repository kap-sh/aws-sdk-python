"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteRentalMode``."""

from typing import Literal, TypeAlias, cast

RouteRentalMode: TypeAlias = Literal[
    "All",
    "Car",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteRentalMode) -> str:
    return value


def deserialize_json(data: str) -> RouteRentalMode:
    return cast(RouteRentalMode, data)
