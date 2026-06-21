"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixTravelMode``."""

from typing import Literal, TypeAlias, cast

RouteMatrixTravelMode: TypeAlias = Literal[
    "Car",
    "Pedestrian",
    "Scooter",
    "Truck",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixTravelMode) -> str:
    return value


def deserialize_json(data: str) -> RouteMatrixTravelMode:
    return cast(RouteMatrixTravelMode, data)
