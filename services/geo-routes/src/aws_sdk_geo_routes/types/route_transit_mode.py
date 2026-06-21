"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitMode``."""

from typing import Literal, TypeAlias, cast

RouteTransitMode: TypeAlias = Literal[
    "AerialTramway",
    "Airplane",
    "All",
    "Bus",
    "BusRapidTransit",
    "CityTrain",
    "Ferry",
    "FunicularRailway",
    "HighSpeedTrain",
    "IntercityTrain",
    "InterregionalTrain",
    "LightRail",
    "Monorail",
    "PrivateBus",
    "RegionalTrain",
    "Subway",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitMode) -> str:
    return value


def deserialize_json(data: str) -> RouteTransitMode:
    return cast(RouteTransitMode, data)
