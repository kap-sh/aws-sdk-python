"""Generated from Smithy shape ``com.amazonaws.quicksight#TooltipItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.tooltip_item

TooltipItemList: TypeAlias = list["capo_quicksight.types.tooltip_item.TooltipItem"]


# --- restJson1 ser/de ---
def serialize_json(value: TooltipItemList) -> list:
    import capo_quicksight.types.tooltip_item

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.tooltip_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> TooltipItemList:
    import capo_quicksight.types.tooltip_item

    out: TooltipItemList = []
    for item in data:
        out.append(capo_quicksight.types.tooltip_item.deserialize_json(item))
    return out
