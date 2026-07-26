"""Generated from Smithy shape ``com.amazonaws.quicksight#BoxPlotFillStyle``."""

from typing import Literal, TypeAlias, cast

BoxPlotFillStyle: TypeAlias = Literal[
    "SOLID",
    "TRANSPARENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: BoxPlotFillStyle) -> str:
    return value


def deserialize_json(data: str) -> BoxPlotFillStyle:
    return cast(BoxPlotFillStyle, data)
