"""Generated from Smithy shape ``com.amazonaws.quicksight#BarChartOrientation``."""

from typing import Literal, TypeAlias, cast

BarChartOrientation: TypeAlias = Literal[
    "HORIZONTAL",
    "VERTICAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: BarChartOrientation) -> str:
    return value


def deserialize_json(data: str) -> BarChartOrientation:
    return cast(BarChartOrientation, data)
