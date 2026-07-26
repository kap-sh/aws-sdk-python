"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferProductIdFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.offer_product_id_string

OfferProductIdFilterValueList: TypeAlias = list[
    "capo_marketplace_catalog.types.offer_product_id_string.OfferProductIdString"
]


# --- restJson1 ser/de ---
def serialize_json(value: OfferProductIdFilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> OfferProductIdFilterValueList:
    return list(data)
