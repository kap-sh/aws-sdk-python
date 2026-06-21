"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleMode``."""

from typing import Literal, TypeAlias, cast

RouteVehicleMode: TypeAlias = Literal[
    "All",
    "Car",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteVehicleMode) -> str:
    return value


def deserialize_json(data: str) -> RouteVehicleMode:
    return cast(RouteVehicleMode, data)
