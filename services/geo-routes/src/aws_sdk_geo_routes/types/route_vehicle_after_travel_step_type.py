"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteVehicleAfterTravelStepType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RouteVehicleAfterTravelStepType: TypeAlias = Literal["Park",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Park",))


def serialize_json(value: RouteVehicleAfterTravelStepType) -> str:
    return value


def deserialize_json(data: str) -> RouteVehicleAfterTravelStepType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RouteVehicleAfterTravelStepType value: {data!r}"
        )
    return cast(RouteVehicleAfterTravelStepType, data)
