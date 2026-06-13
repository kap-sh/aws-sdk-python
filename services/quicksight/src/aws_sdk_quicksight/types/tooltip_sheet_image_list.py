"""Generated from Smithy shape ``com.amazonaws.quicksight#TooltipSheetImageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.sheet_image

TooltipSheetImageList: TypeAlias = list[
    "aws_sdk_quicksight.types.sheet_image.SheetImage"
]


# --- restJson1 ser/de ---
def serialize_json(value: TooltipSheetImageList) -> list:
    import aws_sdk_quicksight.types.sheet_image

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.sheet_image.serialize_json(item))
    return out


def deserialize_json(data: list) -> TooltipSheetImageList:
    import aws_sdk_quicksight.types.sheet_image

    out: TooltipSheetImageList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.sheet_image.deserialize_json(item))
    return out
