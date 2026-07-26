"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationConstraint``."""

from typing import Literal, TypeAlias, cast

WaypointOptimizationConstraint: TypeAlias = Literal[
    "AccessHours",
    "AppointmentTime",
    "Before",
    "Heading",
    "ServiceDuration",
    "SideOfStreet",
]


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationConstraint) -> str:
    return value


def deserialize_json(data: str) -> WaypointOptimizationConstraint:
    return cast(WaypointOptimizationConstraint, data)
