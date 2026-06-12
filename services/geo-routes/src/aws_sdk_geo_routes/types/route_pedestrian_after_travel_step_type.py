"""Generated from Smithy shape ``com.amazonaws.georoutes#RoutePedestrianAfterTravelStepType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RoutePedestrianAfterTravelStepType: TypeAlias = Literal["Wait",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Wait",))


def serialize_json(value: RoutePedestrianAfterTravelStepType) -> str:
    return value


def deserialize_json(data: str) -> RoutePedestrianAfterTravelStepType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RoutePedestrianAfterTravelStepType value: {data!r}"
        )
    return cast(RoutePedestrianAfterTravelStepType, data)
