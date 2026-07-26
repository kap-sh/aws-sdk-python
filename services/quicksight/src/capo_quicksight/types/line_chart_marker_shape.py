"""Generated from Smithy shape ``com.amazonaws.quicksight#LineChartMarkerShape``."""

from typing import Literal, TypeAlias, cast

LineChartMarkerShape: TypeAlias = Literal[
    "CIRCLE",
    "TRIANGLE",
    "SQUARE",
    "DIAMOND",
    "ROUNDED_SQUARE",
]


# --- restJson1 ser/de ---
def serialize_json(value: LineChartMarkerShape) -> str:
    return value


def deserialize_json(data: str) -> LineChartMarkerShape:
    return cast(LineChartMarkerShape, data)
