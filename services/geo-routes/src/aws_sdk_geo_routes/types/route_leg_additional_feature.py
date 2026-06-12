"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteLegAdditionalFeature``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteLegAdditionalFeature: TypeAlias = Literal[
    "Elevation",
    "Incidents",
    "PassThroughWaypoints",
    "Summary",
    "Tolls",
    "TravelStepInstructions",
    "TruckRoadTypes",
    "TypicalDuration",
    "Zones",
    "Bookings",
    "IntermediateStops",
    "NextDepartures",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Elevation",
        "Incidents",
        "PassThroughWaypoints",
        "Summary",
        "Tolls",
        "TravelStepInstructions",
        "TruckRoadTypes",
        "TypicalDuration",
        "Zones",
        "Bookings",
        "IntermediateStops",
        "NextDepartures",
    )
)


def serialize_json(value: RouteLegAdditionalFeature) -> str:
    return value


def deserialize_json(data: str) -> RouteLegAdditionalFeature:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteLegAdditionalFeature value: {data!r}")
    return cast(RouteLegAdditionalFeature, data)
