"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleIncidentSeverity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteVehicleIncidentSeverity: TypeAlias = Literal[
    "Critical",
    "High",
    "Medium",
    "Low",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Critical",
        "High",
        "Medium",
        "Low",
    )
)


def serialize_json(value: RouteVehicleIncidentSeverity) -> str:
    return value


def deserialize_json(data: str) -> RouteVehicleIncidentSeverity:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RouteVehicleIncidentSeverity value: {data!r}"
        )
    return cast(RouteVehicleIncidentSeverity, data)
