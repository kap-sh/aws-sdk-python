"""Generated from Smithy shape ``com.amazonaws.billingconductor#CustomLineItemType``."""

from typing import Literal, TypeAlias, cast

CustomLineItemType: TypeAlias = Literal[
    "CREDIT",
    "FEE",
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomLineItemType) -> str:
    return value


def deserialize_json(data: str) -> CustomLineItemType:
    return cast(CustomLineItemType, data)
