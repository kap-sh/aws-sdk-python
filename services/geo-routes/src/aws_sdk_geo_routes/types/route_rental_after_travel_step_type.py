"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteRentalAfterTravelStepType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteRentalAfterTravelStepType: TypeAlias = Literal["Park",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Park",))


def serialize_json(value: RouteRentalAfterTravelStepType) -> str:
    return value


def deserialize_json(data: str) -> RouteRentalAfterTravelStepType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RouteRentalAfterTravelStepType value: {data!r}"
        )
    return cast(RouteRentalAfterTravelStepType, data)
