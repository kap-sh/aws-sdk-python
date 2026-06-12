"""Generated from Smithy shape ``com.amazonaws.georoutes#RoutePedestrianTravelStepType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RoutePedestrianTravelStepType: TypeAlias = Literal[
    "Arrive",
    "Continue",
    "Depart",
    "Keep",
    "RoundaboutEnter",
    "RoundaboutExit",
    "RoundaboutPass",
    "Turn",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Arrive",
        "Continue",
        "Depart",
        "Keep",
        "RoundaboutEnter",
        "RoundaboutExit",
        "RoundaboutPass",
        "Turn",
    )
)


def serialize_json(value: RoutePedestrianTravelStepType) -> str:
    return value


def deserialize_json(data: str) -> RoutePedestrianTravelStepType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RoutePedestrianTravelStepType value: {data!r}"
        )
    return cast(RoutePedestrianTravelStepType, data)
