"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteFerryBeforeTravelStepType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteFerryBeforeTravelStepType: TypeAlias = Literal["Board",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Board",))


def serialize_json(value: RouteFerryBeforeTravelStepType) -> str:
    return value


def deserialize_json(data: str) -> RouteFerryBeforeTravelStepType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RouteFerryBeforeTravelStepType value: {data!r}"
        )
    return cast(RouteFerryBeforeTravelStepType, data)
