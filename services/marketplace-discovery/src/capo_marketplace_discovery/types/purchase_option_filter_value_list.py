"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PurchaseOptionFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.purchase_option_filter_value

PurchaseOptionFilterValueList: TypeAlias = list[
    "capo_marketplace_discovery.types.purchase_option_filter_value.PurchaseOptionFilterValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: PurchaseOptionFilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> PurchaseOptionFilterValueList:
    return list(data)
