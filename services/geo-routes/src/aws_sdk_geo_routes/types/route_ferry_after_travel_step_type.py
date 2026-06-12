"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteFerryAfterTravelStepType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteFerryAfterTravelStepType: TypeAlias = Literal["Deboard",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Deboard",))


def serialize_json(value: RouteFerryAfterTravelStepType) -> str:
    return value


def deserialize_json(data: str) -> RouteFerryAfterTravelStepType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RouteFerryAfterTravelStepType value: {data!r}"
        )
    return cast(RouteFerryAfterTravelStepType, data)
