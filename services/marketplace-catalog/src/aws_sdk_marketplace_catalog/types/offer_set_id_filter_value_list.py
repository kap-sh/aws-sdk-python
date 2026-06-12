"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferSetIdFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.offer_set_id_string

OfferSetIdFilterValueList: TypeAlias = list[
    "aws_sdk_marketplace_catalog.types.offer_set_id_string.OfferSetIdString"
]


# --- restJson1 ser/de ---
def serialize_json(value: OfferSetIdFilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> OfferSetIdFilterValueList:
    return list(data)
