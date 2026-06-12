"""Generated from Smithy shape ``com.amazonaws.billingconductor#CustomLineItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.custom_line_item_list_element

CustomLineItemList: TypeAlias = list[
    "aws_sdk_billingconductor.types.custom_line_item_list_element.CustomLineItemListElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomLineItemList) -> list:
    import aws_sdk_billingconductor.types.custom_line_item_list_element

    out: list = []
    for item in value:
        out.append(
            aws_sdk_billingconductor.types.custom_line_item_list_element.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CustomLineItemList:
    import aws_sdk_billingconductor.types.custom_line_item_list_element

    out: CustomLineItemList = []
    for item in data:
        out.append(
            aws_sdk_billingconductor.types.custom_line_item_list_element.deserialize_json(
                item
            )
        )
    return out
