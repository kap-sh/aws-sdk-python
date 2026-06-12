"""Generated from Smithy shape ``com.amazonaws.georoutes#RoadSnapTravelMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

RoadSnapTravelMode: TypeAlias = Literal[
    "Car",
    "Pedestrian",
    "Scooter",
    "Truck",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Car",
        "Pedestrian",
        "Scooter",
        "Truck",
    )
)


def serialize_json(value: RoadSnapTravelMode) -> str:
    return value


def deserialize_json(data: str) -> RoadSnapTravelMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RoadSnapTravelMode value: {data!r}")
    return cast(RoadSnapTravelMode, data)
