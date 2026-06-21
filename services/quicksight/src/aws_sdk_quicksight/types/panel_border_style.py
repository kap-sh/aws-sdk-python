"""Generated from Smithy shape ``com.amazonaws.quicksight#PanelBorderStyle``."""

from typing import Literal, TypeAlias, cast

PanelBorderStyle: TypeAlias = Literal[
    "SOLID",
    "DASHED",
    "DOTTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PanelBorderStyle) -> str:
    return value


def deserialize_json(data: str) -> PanelBorderStyle:
    return cast(PanelBorderStyle, data)
