"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleTravelStepType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteVehicleTravelStepType: TypeAlias = Literal[
    "Arrive",
    "Continue",
    "ContinueHighway",
    "Depart",
    "EnterHighway",
    "Exit",
    "Keep",
    "Ramp",
    "RoundaboutEnter",
    "RoundaboutExit",
    "RoundaboutPass",
    "Turn",
    "UTurn",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Arrive",
        "Continue",
        "ContinueHighway",
        "Depart",
        "EnterHighway",
        "Exit",
        "Keep",
        "Ramp",
        "RoundaboutEnter",
        "RoundaboutExit",
        "RoundaboutPass",
        "Turn",
        "UTurn",
    )
)


def serialize_json(value: RouteVehicleTravelStepType) -> str:
    return value


def deserialize_json(data: str) -> RouteVehicleTravelStepType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RouteVehicleTravelStepType value: {data!r}"
        )
    return cast(RouteVehicleTravelStepType, data)
