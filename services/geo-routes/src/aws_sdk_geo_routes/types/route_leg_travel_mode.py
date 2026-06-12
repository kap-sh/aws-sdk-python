"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteLegTravelMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: RouteLegTravelMode) -> str:
    return value


def deserialize_json(data: str) -> RouteLegTravelMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteLegTravelMode value: {data!r}")
    return cast(RouteLegTravelMode, data)
