"""Generated from Smithy shape ``com.amazonaws.billingconductor#CustomLineItemArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billingconductor.types.custom_line_item_arn

CustomLineItemArns: TypeAlias = list[
    "capo_billingconductor.types.custom_line_item_arn.CustomLineItemArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomLineItemArns) -> list:
    return list(value)


def deserialize_json(data: list) -> CustomLineItemArns:
    return list(data)
