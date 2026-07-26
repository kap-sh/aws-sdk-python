"""Generated from Smithy shape ``com.amazonaws.billingconductor#CustomLineItemBatchDisassociationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billingconductor.types.custom_line_item_association_element

CustomLineItemBatchDisassociationsList: TypeAlias = list[
    "capo_billingconductor.types.custom_line_item_association_element.CustomLineItemAssociationElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomLineItemBatchDisassociationsList) -> list:
    return list(value)


def deserialize_json(data: list) -> CustomLineItemBatchDisassociationsList:
    return list(data)
