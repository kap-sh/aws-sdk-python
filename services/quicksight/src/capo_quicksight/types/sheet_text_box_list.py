"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetTextBoxList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.sheet_text_box

SheetTextBoxList: TypeAlias = list["capo_quicksight.types.sheet_text_box.SheetTextBox"]


# --- restJson1 ser/de ---
def serialize_json(value: SheetTextBoxList) -> list:
    import capo_quicksight.types.sheet_text_box

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.sheet_text_box.serialize_json(item))
    return out


def deserialize_json(data: list) -> SheetTextBoxList:
    import capo_quicksight.types.sheet_text_box

    out: SheetTextBoxList = []
    for item in data:
        out.append(capo_quicksight.types.sheet_text_box.deserialize_json(item))
    return out
