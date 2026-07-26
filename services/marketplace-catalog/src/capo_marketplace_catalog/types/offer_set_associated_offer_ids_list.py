"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferSetAssociatedOfferIdsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.offer_set_associated_offer_ids_string

OfferSetAssociatedOfferIdsList: TypeAlias = list[
    "capo_marketplace_catalog.types.offer_set_associated_offer_ids_string.OfferSetAssociatedOfferIdsString"
]


# --- restJson1 ser/de ---
def serialize_json(value: OfferSetAssociatedOfferIdsList) -> list:
    return list(value)


def deserialize_json(data: list) -> OfferSetAssociatedOfferIdsList:
    return list(data)
