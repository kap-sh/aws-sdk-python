"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetControlLayoutList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.sheet_control_layout

SheetControlLayoutList: TypeAlias = list[
    "aws_sdk_quicksight.types.sheet_control_layout.SheetControlLayout"
]


# --- restJson1 ser/de ---
def serialize_json(value: SheetControlLayoutList) -> list:
    import aws_sdk_quicksight.types.sheet_control_layout

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.sheet_control_layout.serialize_json(item))
    return out


def deserialize_json(data: list) -> SheetControlLayoutList:
    import aws_sdk_quicksight.types.sheet_control_layout

    out: SheetControlLayoutList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.sheet_control_layout.deserialize_json(item))
    return out
