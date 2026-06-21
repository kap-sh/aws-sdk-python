"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PurchaseOptionBadgeType``."""

from typing import Literal, TypeAlias, cast

PurchaseOptionBadgeType: TypeAlias = Literal[
    "PRIVATE_PRICING",
    "FUTURE_DATED",
    "REPLACEMENT_OFFER",
]


# --- restJson1 ser/de ---
def serialize_json(value: PurchaseOptionBadgeType) -> str:
    return value


def deserialize_json(data: str) -> PurchaseOptionBadgeType:
    return cast(PurchaseOptionBadgeType, data)
