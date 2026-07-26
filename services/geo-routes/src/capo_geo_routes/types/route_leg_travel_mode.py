"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteLegTravelMode``."""

from typing import Literal, TypeAlias, cast

RouteLegTravelMode: TypeAlias = Literal[
    "Car",
    "Ferry",
    "Pedestrian",
    "Scooter",
    "Truck",
    "CarShuttleTrain",
    "AerialTramway",
    "Airplane",
    "Bus",
    "BusRapidTransit",
    "CityTrain",
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
def serialize_json(value: RouteLegTravelMode) -> str:
    return value


def deserialize_json(data: str) -> RouteLegTravelMode:
    return cast(RouteLegTravelMode, data)
