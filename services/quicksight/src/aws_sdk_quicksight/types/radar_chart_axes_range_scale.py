"""Generated from Smithy shape ``com.amazonaws.quicksight#RadarChartAxesRangeScale``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

RadarChartAxesRangeScale: TypeAlias = Literal[
    "AUTO",
    "INDEPENDENT",
    "SHARED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO",
        "INDEPENDENT",
        "SHARED",
    )
)


def serialize_json(value: RadarChartAxesRangeScale) -> str:
    return value


def deserialize_json(data: str) -> RadarChartAxesRangeScale:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RadarChartAxesRangeScale value: {data!r}")
    return cast(RadarChartAxesRangeScale, data)
