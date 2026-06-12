"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleIncidentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: RouteVehicleIncidentType) -> str:
    return value


def deserialize_json(data: str) -> RouteVehicleIncidentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteVehicleIncidentType value: {data!r}")
    return cast(RouteVehicleIncidentType, data)
