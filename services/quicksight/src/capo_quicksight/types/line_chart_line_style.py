"""Generated from Smithy shape ``com.amazonaws.quicksight#LineChartLineStyle``."""

from typing import Literal, TypeAlias, cast

LineChartLineStyle: TypeAlias = Literal[
    "SOLID",
    "DOTTED",
    "DASHED",
]


# --- restJson1 ser/de ---
def serialize_json(value: LineChartLineStyle) -> str:
    return value


def deserialize_json(data: str) -> LineChartLineStyle:
    return cast(LineChartLineStyle, data)
