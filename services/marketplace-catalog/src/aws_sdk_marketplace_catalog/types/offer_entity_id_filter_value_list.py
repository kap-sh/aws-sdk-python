"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferEntityIdFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.offer_entity_id_string

OfferEntityIdFilterValueList: TypeAlias = list[
    "aws_sdk_marketplace_catalog.types.offer_entity_id_string.OfferEntityIdString"
]


# --- restJson1 ser/de ---
def serialize_json(value: OfferEntityIdFilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> OfferEntityIdFilterValueList:
    return list(data)
