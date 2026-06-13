"""Generated from Smithy shape ``com.amazonaws.quicksight#LayoutList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.layout

LayoutList: TypeAlias = list["aws_sdk_quicksight.types.layout.Layout"]


# --- restJson1 ser/de ---
def serialize_json(value: LayoutList) -> list:
    import aws_sdk_quicksight.types.layout

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.layout.serialize_json(item))
    return out


def deserialize_json(data: list) -> LayoutList:
    import aws_sdk_quicksight.types.layout

    out: LayoutList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.layout.deserialize_json(item))
    return out
