"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitIncidentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: RouteTransitIncidentType) -> str:
    return value


def deserialize_json(data: str) -> RouteTransitIncidentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteTransitIncidentType value: {data!r}")
    return cast(RouteTransitIncidentType, data)
