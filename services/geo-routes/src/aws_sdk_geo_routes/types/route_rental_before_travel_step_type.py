"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteRentalBeforeTravelStepType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteRentalBeforeTravelStepType: TypeAlias = Literal["Setup",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Setup",))


def serialize_json(value: RouteRentalBeforeTravelStepType) -> str:
    return value


def deserialize_json(data: str) -> RouteRentalBeforeTravelStepType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RouteRentalBeforeTravelStepType value: {data!r}"
        )
    return cast(RouteRentalBeforeTravelStepType, data)
