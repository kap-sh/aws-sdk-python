"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SellerEngagementList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.seller_engagement

SellerEngagementList: TypeAlias = list[
    "capo_marketplace_discovery.types.seller_engagement.SellerEngagement"
]


# --- restJson1 ser/de ---
def serialize_json(value: SellerEngagementList) -> list:
    import capo_marketplace_discovery.types.seller_engagement

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_discovery.types.seller_engagement.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SellerEngagementList:
    import capo_marketplace_discovery.types.seller_engagement

    out: SellerEngagementList = []
    for item in data:
        out.append(
            capo_marketplace_discovery.types.seller_engagement.deserialize_json(item)
        )
    return out
