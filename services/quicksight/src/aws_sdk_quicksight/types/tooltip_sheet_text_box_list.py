"""Generated from Smithy shape ``com.amazonaws.quicksight#TooltipSheetTextBoxList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.sheet_text_box

TooltipSheetTextBoxList: TypeAlias = list[
    "aws_sdk_quicksight.types.sheet_text_box.SheetTextBox"
]


# --- restJson1 ser/de ---
def serialize_json(value: TooltipSheetTextBoxList) -> list:
    import aws_sdk_quicksight.types.sheet_text_box

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.sheet_text_box.serialize_json(item))
    return out


def deserialize_json(data: list) -> TooltipSheetTextBoxList:
    import aws_sdk_quicksight.types.sheet_text_box

    out: TooltipSheetTextBoxList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.sheet_text_box.deserialize_json(item))
    return out
