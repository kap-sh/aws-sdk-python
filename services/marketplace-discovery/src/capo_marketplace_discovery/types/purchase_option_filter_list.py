"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PurchaseOptionFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.purchase_option_filter

PurchaseOptionFilterList: TypeAlias = list[
    "capo_marketplace_discovery.types.purchase_option_filter.PurchaseOptionFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: PurchaseOptionFilterList) -> list:
    import capo_marketplace_discovery.types.purchase_option_filter

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_discovery.types.purchase_option_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PurchaseOptionFilterList:
    import capo_marketplace_discovery.types.purchase_option_filter

    out: PurchaseOptionFilterList = []
    for item in data:
        out.append(
            capo_marketplace_discovery.types.purchase_option_filter.deserialize_json(
                item
            )
        )
    return out
