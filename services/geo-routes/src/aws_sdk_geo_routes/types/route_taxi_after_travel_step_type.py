"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTaxiAfterTravelStepType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteTaxiAfterTravelStepType: TypeAlias = Literal["Park",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Park",))


def serialize_json(value: RouteTaxiAfterTravelStepType) -> str:
    return value


def deserialize_json(data: str) -> RouteTaxiAfterTravelStepType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RouteTaxiAfterTravelStepType value: {data!r}"
        )
    return cast(RouteTaxiAfterTravelStepType, data)
