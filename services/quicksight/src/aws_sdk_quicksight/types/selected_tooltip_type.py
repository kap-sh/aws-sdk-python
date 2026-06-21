"""Generated from Smithy shape ``com.amazonaws.quicksight#SelectedTooltipType``."""

from typing import Literal, TypeAlias, cast

SelectedTooltipType: TypeAlias = Literal[
    "BASIC",
    "DETAILED",
    "SHEET",
]


# --- restJson1 ser/de ---
def serialize_json(value: SelectedTooltipType) -> str:
    return value


def deserialize_json(data: str) -> SelectedTooltipType:
    return cast(SelectedTooltipType, data)
