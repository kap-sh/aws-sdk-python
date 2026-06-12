"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTransitTravelStepType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteTransitTravelStepType: TypeAlias = Literal["Depart",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Depart",))


def serialize_json(value: RouteTransitTravelStepType) -> str:
    return value


def deserialize_json(data: str) -> RouteTransitTravelStepType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RouteTransitTravelStepType value: {data!r}"
        )
    return cast(RouteTransitTravelStepType, data)
