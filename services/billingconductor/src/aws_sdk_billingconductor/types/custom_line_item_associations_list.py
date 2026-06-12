"""Generated from Smithy shape ``com.amazonaws.billingconductor#CustomLineItemAssociationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.custom_line_item_association_element

CustomLineItemAssociationsList: TypeAlias = list[
    "aws_sdk_billingconductor.types.custom_line_item_association_element.CustomLineItemAssociationElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomLineItemAssociationsList) -> list:
    return list(value)


def deserialize_json(data: list) -> CustomLineItemAssociationsList:
    return list(data)
