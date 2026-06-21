"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTollVehicleCategory``."""

from typing import Literal, TypeAlias, cast

RouteTollVehicleCategory: TypeAlias = Literal["Minibus",]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTollVehicleCategory) -> str:
    return value


def deserialize_json(data: str) -> RouteTollVehicleCategory:
    return cast(RouteTollVehicleCategory, data)
