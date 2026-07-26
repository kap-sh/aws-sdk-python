"""Generated from Smithy shape ``com.amazonaws.billingconductor#ResponsibilityTransferArnsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billingconductor.types.responsibility_transfer_arn

ResponsibilityTransferArnsList: TypeAlias = list[
    "capo_billingconductor.types.responsibility_transfer_arn.ResponsibilityTransferArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResponsibilityTransferArnsList) -> list:
    return list(value)


def deserialize_json(data: list) -> ResponsibilityTransferArnsList:
    return list(data)
