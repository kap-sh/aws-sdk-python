"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PurchaseOptionBadgeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.purchase_option_badge

PurchaseOptionBadgeList: TypeAlias = list[
    "aws_sdk_marketplace_discovery.types.purchase_option_badge.PurchaseOptionBadge"
]


# --- restJson1 ser/de ---
def serialize_json(value: PurchaseOptionBadgeList) -> list:
    import aws_sdk_marketplace_discovery.types.purchase_option_badge

    out: list = []
    for item in value:
        out.append(
            aws_sdk_marketplace_discovery.types.purchase_option_badge.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> PurchaseOptionBadgeList:
    import aws_sdk_marketplace_discovery.types.purchase_option_badge

    out: PurchaseOptionBadgeList = []
    for item in data:
        out.append(
            aws_sdk_marketplace_discovery.types.purchase_option_badge.deserialize_json(
                item
            )
        )
    return out
