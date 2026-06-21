"""Generated from Smithy shape ``com.amazonaws.quicksight#VisualCustomActionTrigger``."""

from typing import Literal, TypeAlias, cast

VisualCustomActionTrigger: TypeAlias = Literal[
    "DATA_POINT_CLICK",
    "DATA_POINT_MENU",
]


# --- restJson1 ser/de ---
def serialize_json(value: VisualCustomActionTrigger) -> str:
    return value


def deserialize_json(data: str) -> VisualCustomActionTrigger:
    return cast(VisualCustomActionTrigger, data)
