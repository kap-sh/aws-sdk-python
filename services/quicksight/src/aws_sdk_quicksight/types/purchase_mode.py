"""Generated from Smithy shape ``com.amazonaws.quicksight#PurchaseMode``."""

from typing import Literal, TypeAlias, cast

PurchaseMode: TypeAlias = Literal[
    "MANUAL",
    "AUTO_PURCHASE",
]


# --- restJson1 ser/de ---
def serialize_json(value: PurchaseMode) -> str:
    return value


def deserialize_json(data: str) -> PurchaseMode:
    return cast(PurchaseMode, data)
