"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ListingAssociatedEntityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.listing_associated_entity

ListingAssociatedEntityList: TypeAlias = list[
    "capo_marketplace_discovery.types.listing_associated_entity.ListingAssociatedEntity"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListingAssociatedEntityList) -> list:
    import capo_marketplace_discovery.types.listing_associated_entity

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_discovery.types.listing_associated_entity.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListingAssociatedEntityList:
    import capo_marketplace_discovery.types.listing_associated_entity

    out: ListingAssociatedEntityList = []
    for item in data:
        out.append(
            capo_marketplace_discovery.types.listing_associated_entity.deserialize_json(
                item
            )
        )
    return out
