"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteLegAdditionalFeature``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: RouteLegAdditionalFeature) -> str:
    return value


def deserialize_json(data: str) -> RouteLegAdditionalFeature:
    return cast(RouteLegAdditionalFeature, data)
