"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixTruckType``."""

from typing import Literal, TypeAlias, cast

RouteMatrixTruckType: TypeAlias = Literal[
    "LightTruck",
    "StraightTruck",
    "Tractor",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixTruckType) -> str:
    return value


def deserialize_json(data: str) -> RouteMatrixTruckType:
    return cast(RouteMatrixTruckType, data)
