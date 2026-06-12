"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitAfterTravelStepType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteTransitAfterTravelStepType: TypeAlias = Literal["Deboard",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Deboard",))


def serialize_json(value: RouteTransitAfterTravelStepType) -> str:
    return value


def deserialize_json(data: str) -> RouteTransitAfterTravelStepType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RouteTransitAfterTravelStepType value: {data!r}"
        )
    return cast(RouteTransitAfterTravelStepType, data)
