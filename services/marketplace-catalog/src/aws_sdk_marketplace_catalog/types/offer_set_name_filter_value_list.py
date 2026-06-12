"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferSetNameFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.offer_set_name_string

OfferSetNameFilterValueList: TypeAlias = list[
    "aws_sdk_marketplace_catalog.types.offer_set_name_string.OfferSetNameString"
]


# --- restJson1 ser/de ---
def serialize_json(value: OfferSetNameFilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> OfferSetNameFilterValueList:
    return list(data)
