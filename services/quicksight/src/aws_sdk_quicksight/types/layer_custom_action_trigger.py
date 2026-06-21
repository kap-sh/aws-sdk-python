"""Generated from Smithy shape ``com.amazonaws.quicksight#LayerCustomActionTrigger``."""

from typing import Literal, TypeAlias, cast

LayerCustomActionTrigger: TypeAlias = Literal[
    "DATA_POINT_CLICK",
    "DATA_POINT_MENU",
]


# --- restJson1 ser/de ---
def serialize_json(value: LayerCustomActionTrigger) -> str:
    return value


def deserialize_json(data: str) -> LayerCustomActionTrigger:
    return cast(LayerCustomActionTrigger, data)
