"""Generated from Smithy shape ``com.amazonaws.quicksight#HistogramBinType``."""

from typing import Literal, TypeAlias, cast

HistogramBinType: TypeAlias = Literal[
    "BIN_COUNT",
    "BIN_WIDTH",
]


# --- restJson1 ser/de ---
def serialize_json(value: HistogramBinType) -> str:
    return value


def deserialize_json(data: str) -> HistogramBinType:
    return cast(HistogramBinType, data)
