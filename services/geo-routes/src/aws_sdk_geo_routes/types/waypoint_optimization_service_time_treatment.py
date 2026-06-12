"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationServiceTimeTreatment``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

WaypointOptimizationServiceTimeTreatment: TypeAlias = Literal[
    "Rest",
    "Work",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Rest",
        "Work",
    )
)


def serialize_json(value: WaypointOptimizationServiceTimeTreatment) -> str:
    return value


def deserialize_json(data: str) -> WaypointOptimizationServiceTimeTreatment:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown WaypointOptimizationServiceTimeTreatment value: {data!r}"
        )
    return cast(WaypointOptimizationServiceTimeTreatment, data)
