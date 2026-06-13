"""Generated from Smithy shape ``com.amazonaws.quicksight#RadarChartShape``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

RadarChartShape: TypeAlias = Literal[
    "CIRCLE",
    "POLYGON",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CIRCLE",
        "POLYGON",
    )
)


def serialize_json(value: RadarChartShape) -> str:
    return value


def deserialize_json(data: str) -> RadarChartShape:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RadarChartShape value: {data!r}")
    return cast(RadarChartShape, data)
