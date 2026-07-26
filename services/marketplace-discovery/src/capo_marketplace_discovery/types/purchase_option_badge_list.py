"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PurchaseOptionBadgeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.purchase_option_badge

PurchaseOptionBadgeList: TypeAlias = list[
    "capo_marketplace_discovery.types.purchase_option_badge.PurchaseOptionBadge"
]


# --- restJson1 ser/de ---
def serialize_json(value: PurchaseOptionBadgeList) -> list:
    import capo_marketplace_discovery.types.purchase_option_badge

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_discovery.types.purchase_option_badge.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PurchaseOptionBadgeList:
    import capo_marketplace_discovery.types.purchase_option_badge

    out: PurchaseOptionBadgeList = []
    for item in data:
        out.append(
            capo_marketplace_discovery.types.purchase_option_badge.deserialize_json(
                item
            )
        )
    return out
