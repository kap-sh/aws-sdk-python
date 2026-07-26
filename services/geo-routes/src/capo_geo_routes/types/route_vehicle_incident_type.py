"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleIncidentType``."""

from typing import Literal, TypeAlias, cast

RouteVehicleIncidentType: TypeAlias = Literal[
    "Accident",
    "Congestion",
    "Construction",
    "DisabledVehicle",
    "LaneRestriction",
    "MassTransit",
    "Other",
    "PlannedEvent",
    "RoadClosure",
    "RoadHazard",
    "Weather",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteVehicleIncidentType) -> str:
    return value


def deserialize_json(data: str) -> RouteVehicleIncidentType:
    return cast(RouteVehicleIncidentType, data)
