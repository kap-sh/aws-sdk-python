"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationServiceTimeTreatment``."""

from typing import Literal, TypeAlias, cast

WaypointOptimizationServiceTimeTreatment: TypeAlias = Literal[
    "Rest",
    "Work",
]


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationServiceTimeTreatment) -> str:
    return value


def deserialize_json(data: str) -> WaypointOptimizationServiceTimeTreatment:
    return cast(WaypointOptimizationServiceTimeTreatment, data)
