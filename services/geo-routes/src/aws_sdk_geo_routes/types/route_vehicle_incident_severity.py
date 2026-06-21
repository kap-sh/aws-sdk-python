"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleIncidentSeverity``."""

from typing import Literal, TypeAlias, cast

RouteVehicleIncidentSeverity: TypeAlias = Literal[
    "Critical",
    "High",
    "Medium",
    "Low",
]


# --- restJson1 ser/de ---
def serialize_json(value: RouteVehicleIncidentSeverity) -> str:
    return value


def deserialize_json(data: str) -> RouteVehicleIncidentSeverity:
    return cast(RouteVehicleIncidentSeverity, data)
