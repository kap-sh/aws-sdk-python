"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationConstraint``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

WaypointOptimizationConstraint: TypeAlias = Literal[
    "AccessHours",
    "AppointmentTime",
    "Before",
    "Heading",
    "ServiceDuration",
    "SideOfStreet",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AccessHours",
        "AppointmentTime",
        "Before",
        "Heading",
        "ServiceDuration",
        "SideOfStreet",
    )
)


def serialize_json(value: WaypointOptimizationConstraint) -> str:
    return value


def deserialize_json(data: str) -> WaypointOptimizationConstraint:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown WaypointOptimizationConstraint value: {data!r}"
        )
    return cast(WaypointOptimizationConstraint, data)
