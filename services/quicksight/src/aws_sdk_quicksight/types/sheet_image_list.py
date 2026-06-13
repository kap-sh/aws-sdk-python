"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetImageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.sheet_image

SheetImageList: TypeAlias = list["aws_sdk_quicksight.types.sheet_image.SheetImage"]


# --- restJson1 ser/de ---
def serialize_json(value: SheetImageList) -> list:
    import aws_sdk_quicksight.types.sheet_image

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.sheet_image.serialize_json(item))
    return out


def deserialize_json(data: list) -> SheetImageList:
    import aws_sdk_quicksight.types.sheet_image

    out: SheetImageList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.sheet_image.deserialize_json(item))
    return out
