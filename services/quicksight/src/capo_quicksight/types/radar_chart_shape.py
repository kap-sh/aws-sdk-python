"""Generated from Smithy shape ``com.amazonaws.quicksight#RadarChartShape``."""

from typing import Literal, TypeAlias, cast

RadarChartShape: TypeAlias = Literal[
    "CIRCLE",
    "POLYGON",
]


# --- restJson1 ser/de ---
def serialize_json(value: RadarChartShape) -> str:
    return value


def deserialize_json(data: str) -> RadarChartShape:
    return cast(RadarChartShape, data)
