"""Generated from Smithy shape ``com.amazonaws.quicksight#VisualHighlightTrigger``."""

from typing import Literal, TypeAlias, cast

VisualHighlightTrigger: TypeAlias = Literal[
    "DATA_POINT_CLICK",
    "DATA_POINT_HOVER",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: VisualHighlightTrigger) -> str:
    return value


def deserialize_json(data: str) -> VisualHighlightTrigger:
    return cast(VisualHighlightTrigger, data)
