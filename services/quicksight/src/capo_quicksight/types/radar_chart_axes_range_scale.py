"""Generated from Smithy shape ``com.amazonaws.quicksight#RadarChartAxesRangeScale``."""

from typing import Literal, TypeAlias, cast

RadarChartAxesRangeScale: TypeAlias = Literal[
    "AUTO",
    "INDEPENDENT",
    "SHARED",
]


# --- restJson1 ser/de ---
def serialize_json(value: RadarChartAxesRangeScale) -> str:
    return value


def deserialize_json(data: str) -> RadarChartAxesRangeScale:
    return cast(RadarChartAxesRangeScale, data)
