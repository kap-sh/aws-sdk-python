"""Generated from Smithy shape ``com.amazonaws.quicksight#SparklineVisualType``."""

from typing import Literal, TypeAlias, cast

SparklineVisualType: TypeAlias = Literal[
    "LINE",
    "AREA_LINE",
]


# --- restJson1 ser/de ---
def serialize_json(value: SparklineVisualType) -> str:
    return value


def deserialize_json(data: str) -> SparklineVisualType:
    return cast(SparklineVisualType, data)
