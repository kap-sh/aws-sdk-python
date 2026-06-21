"""Generated from Smithy shape ``com.amazonaws.quicksight#ImageCustomActionTrigger``."""

from typing import Literal, TypeAlias, cast

ImageCustomActionTrigger: TypeAlias = Literal[
    "CLICK",
    "MENU",
]


# --- restJson1 ser/de ---
def serialize_json(value: ImageCustomActionTrigger) -> str:
    return value


def deserialize_json(data: str) -> ImageCustomActionTrigger:
    return cast(ImageCustomActionTrigger, data)
