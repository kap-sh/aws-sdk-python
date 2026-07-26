"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ListingSummaryAssociatedEntityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.listing_summary_associated_entity

ListingSummaryAssociatedEntityList: TypeAlias = list[
    "capo_marketplace_discovery.types.listing_summary_associated_entity.ListingSummaryAssociatedEntity"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListingSummaryAssociatedEntityList) -> list:
    import capo_marketplace_discovery.types.listing_summary_associated_entity

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_discovery.types.listing_summary_associated_entity.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListingSummaryAssociatedEntityList:
    import capo_marketplace_discovery.types.listing_summary_associated_entity

    out: ListingSummaryAssociatedEntityList = []
    for item in data:
        out.append(
            capo_marketplace_discovery.types.listing_summary_associated_entity.deserialize_json(
                item
            )
        )
    return out
