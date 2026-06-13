"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ListingBadgeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.listing_badge

ListingBadgeList: TypeAlias = list[
    "aws_sdk_marketplace_discovery.types.listing_badge.ListingBadge"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListingBadgeList) -> list:
    import aws_sdk_marketplace_discovery.types.listing_badge

    out: list = []
    for item in value:
        out.append(
            aws_sdk_marketplace_discovery.types.listing_badge.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListingBadgeList:
    import aws_sdk_marketplace_discovery.types.listing_badge

    out: ListingBadgeList = []
    for item in data:
        out.append(
            aws_sdk_marketplace_discovery.types.listing_badge.deserialize_json(item)
        )
    return out
