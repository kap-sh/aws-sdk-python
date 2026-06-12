"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTaxiBeforeTravelStepType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteTaxiBeforeTravelStepType: TypeAlias = Literal["Wait",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Wait",))


def serialize_json(value: RouteTaxiBeforeTravelStepType) -> str:
    return value


def deserialize_json(data: str) -> RouteTaxiBeforeTravelStepType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RouteTaxiBeforeTravelStepType value: {data!r}"
        )
    return cast(RouteTaxiBeforeTravelStepType, data)
