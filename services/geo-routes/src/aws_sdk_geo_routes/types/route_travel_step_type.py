"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTravelStepType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteTravelStepType: TypeAlias = Literal[
    "Default",
    "TurnByTurn",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Default",
        "TurnByTurn",
    )
)


def serialize_json(value: RouteTravelStepType) -> str:
    return value


def deserialize_json(data: str) -> RouteTravelStepType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RouteTravelStepType value: {data!r}")
    return cast(RouteTravelStepType, data)
