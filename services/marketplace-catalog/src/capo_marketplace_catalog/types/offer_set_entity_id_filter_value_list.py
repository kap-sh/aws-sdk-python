"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferSetEntityIdFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.offer_set_entity_id_string

OfferSetEntityIdFilterValueList: TypeAlias = list[
    "capo_marketplace_catalog.types.offer_set_entity_id_string.OfferSetEntityIdString"
]


# --- restJson1 ser/de ---
def serialize_json(value: OfferSetEntityIdFilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> OfferSetEntityIdFilterValueList:
    return list(data)
