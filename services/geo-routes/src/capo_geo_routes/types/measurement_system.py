"""Generated from Smithy shape ``com.amazonaws.georoutes#MeasurementSystem``."""

from typing import Literal, TypeAlias, cast

MeasurementSystem: TypeAlias = Literal[
    "Metric",
    "Imperial",
]


# --- restJson1 ser/de ---
def serialize_json(value: MeasurementSystem) -> str:
    return value


def deserialize_json(data: str) -> MeasurementSystem:
    return cast(MeasurementSystem, data)
