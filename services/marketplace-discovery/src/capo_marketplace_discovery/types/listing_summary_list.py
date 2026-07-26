"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ListingSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.listing_summary

ListingSummaryList: TypeAlias = list[
    "capo_marketplace_discovery.types.listing_summary.ListingSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListingSummaryList) -> list:
    import capo_marketplace_discovery.types.listing_summary

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_discovery.types.listing_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListingSummaryList:
    import capo_marketplace_discovery.types.listing_summary

    out: ListingSummaryList = []
    for item in data:
        out.append(
            capo_marketplace_discovery.types.listing_summary.deserialize_json(item)
        )
    return out
