"""Generated from Smithy shape ``com.amazonaws.billingconductor#CustomLineItemNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billingconductor.types.custom_line_item_name

CustomLineItemNameList: TypeAlias = list[
    "capo_billingconductor.types.custom_line_item_name.CustomLineItemName"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomLineItemNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> CustomLineItemNameList:
    return list(data)
