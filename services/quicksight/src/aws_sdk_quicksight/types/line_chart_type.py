"""Generated from Smithy shape ``com.amazonaws.quicksight#LineChartType``."""

from typing import Literal, TypeAlias, cast

LineChartType: TypeAlias = Literal[
    "LINE",
    "AREA",
    "STACKED_AREA",
]


# --- restJson1 ser/de ---
def serialize_json(value: LineChartType) -> str:
    return value


def deserialize_json(data: str) -> LineChartType:
    return cast(LineChartType, data)
