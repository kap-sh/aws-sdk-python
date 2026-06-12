"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitBeforeTravelStepType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteTransitBeforeTravelStepType: TypeAlias = Literal["Board",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Board",))


def serialize_json(value: RouteTransitBeforeTravelStepType) -> str:
    return value


def deserialize_json(data: str) -> RouteTransitBeforeTravelStepType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RouteTransitBeforeTravelStepType value: {data!r}"
        )
    return cast(RouteTransitBeforeTravelStepType, data)
