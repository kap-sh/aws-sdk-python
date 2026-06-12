"""Generated from Smithy shape ``com.amazonaws.georoutes#MeasurementSystem``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_geo_routes.errors import DeserializationError

MeasurementSystem: TypeAlias = Literal[
    "Metric",
    "Imperial",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Metric",
        "Imperial",
    )
)


def serialize_json(value: MeasurementSystem) -> str:
    return value


def deserialize_json(data: str) -> MeasurementSystem:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MeasurementSystem value: {data!r}")
    return cast(MeasurementSystem, data)
