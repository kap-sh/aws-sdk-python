"""Generated from Smithy shape ``com.amazonaws.billingconductor#CustomLineItemBatchAssociationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billingconductor.types.custom_line_item_association_element

CustomLineItemBatchAssociationsList: TypeAlias = list[
    "capo_billingconductor.types.custom_line_item_association_element.CustomLineItemAssociationElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomLineItemBatchAssociationsList) -> list:
    return list(value)


def deserialize_json(data: list) -> CustomLineItemBatchAssociationsList:
    return list(data)
