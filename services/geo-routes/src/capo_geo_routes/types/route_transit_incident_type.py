"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitIncidentType``."""

from typing import Literal, TypeAlias, cast

RouteTransitIncidentType: TypeAlias = Literal[
    "Accident",
    "Construction",
    "Demonstration",
    "Holiday",
    "Maintenance",
    "MedicalEmergency",
    "Other",
    "PoliceActivity",
    "Strike",
    "TechnicalProblem",
    "Weather",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteTransitIncidentType) -> str:
    return value


def deserialize_json(data: str) -> RouteTransitIncidentType:
    return cast(RouteTransitIncidentType, data)
