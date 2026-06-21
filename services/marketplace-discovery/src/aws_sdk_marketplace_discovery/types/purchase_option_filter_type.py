"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PurchaseOptionFilterType``."""

from typing import Literal, TypeAlias, cast

PurchaseOptionFilterType: TypeAlias = Literal[
    "PRODUCT_ID",
    "SELLER_OF_RECORD_PROFILE_ID",
    "PURCHASE_OPTION_TYPE",
    "VISIBILITY_SCOPE",
    "AVAILABILITY_STATUS",
]


# --- restJson1 ser/de ---
def serialize_json(value: PurchaseOptionFilterType) -> str:
    return value


def deserialize_json(data: str) -> PurchaseOptionFilterType:
    return cast(PurchaseOptionFilterType, data)
