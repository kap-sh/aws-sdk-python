"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineTravelMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

IsolineTravelMode: TypeAlias = Literal[
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


def serialize_json(value: IsolineTravelMode) -> str:
    return value


def deserialize_json(data: str) -> IsolineTravelMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IsolineTravelMode value: {data!r}")
    return cast(IsolineTravelMode, data)
