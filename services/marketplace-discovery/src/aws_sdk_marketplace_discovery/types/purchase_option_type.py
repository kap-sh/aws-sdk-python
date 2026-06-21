"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PurchaseOptionType``."""

from typing import Literal, TypeAlias, cast

PurchaseOptionType: TypeAlias = Literal[
    "OFFER",
    "OFFERSET",
]


# --- restJson1 ser/de ---
def serialize_json(value: PurchaseOptionType) -> str:
    return value


def deserialize_json(data: str) -> PurchaseOptionType:
    return cast(PurchaseOptionType, data)
