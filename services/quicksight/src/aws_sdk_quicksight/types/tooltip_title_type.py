"""Generated from Smithy shape ``com.amazonaws.quicksight#TooltipTitleType``."""

from typing import Literal, TypeAlias, cast

TooltipTitleType: TypeAlias = Literal[
    "NONE",
    "PRIMARY_VALUE",
]


# --- restJson1 ser/de ---
def serialize_json(value: TooltipTitleType) -> str:
    return value


def deserialize_json(data: str) -> TooltipTitleType:
    return cast(TooltipTitleType, data)
