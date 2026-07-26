"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetControlLayoutList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.sheet_control_layout

SheetControlLayoutList: TypeAlias = list[
    "capo_quicksight.types.sheet_control_layout.SheetControlLayout"
]


# --- restJson1 ser/de ---
def serialize_json(value: SheetControlLayoutList) -> list:
    import capo_quicksight.types.sheet_control_layout

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.sheet_control_layout.serialize_json(item))
    return out


def deserialize_json(data: list) -> SheetControlLayoutList:
    import capo_quicksight.types.sheet_control_layout

    out: SheetControlLayoutList = []
    for item in data:
        out.append(capo_quicksight.types.sheet_control_layout.deserialize_json(item))
    return out
