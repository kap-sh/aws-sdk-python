"""Generated from Smithy shape ``com.amazonaws.quicksight#TooltipSheetVisualList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.visual

TooltipSheetVisualList: TypeAlias = list["aws_sdk_quicksight.types.visual.Visual"]


# --- restJson1 ser/de ---
def serialize_json(value: TooltipSheetVisualList) -> list:
    import aws_sdk_quicksight.types.visual

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.visual.serialize_json(item))
    return out


def deserialize_json(data: list) -> TooltipSheetVisualList:
    import aws_sdk_quicksight.types.visual

    out: TooltipSheetVisualList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.visual.deserialize_json(item))
    return out
