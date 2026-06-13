"""Generated from Smithy shape ``com.amazonaws.quicksight#TooltipItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.tooltip_item

TooltipItemList: TypeAlias = list["aws_sdk_quicksight.types.tooltip_item.TooltipItem"]


# --- restJson1 ser/de ---
def serialize_json(value: TooltipItemList) -> list:
    import aws_sdk_quicksight.types.tooltip_item

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.tooltip_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> TooltipItemList:
    import aws_sdk_quicksight.types.tooltip_item

    out: TooltipItemList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.tooltip_item.deserialize_json(item))
    return out
