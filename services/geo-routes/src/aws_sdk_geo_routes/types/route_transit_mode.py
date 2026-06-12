"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: RouteTransitMode) -> str:
    return value


def deserialize_json(data: str) -> RouteTransitMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteTransitMode value: {data!r}")
    return cast(RouteTransitMode, data)
