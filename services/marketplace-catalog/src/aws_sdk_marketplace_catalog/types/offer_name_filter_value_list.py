"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferNameFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.offer_name_string

OfferNameFilterValueList: TypeAlias = list[
    "aws_sdk_marketplace_catalog.types.offer_name_string.OfferNameString"
]


# --- restJson1 ser/de ---
def serialize_json(value: OfferNameFilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> OfferNameFilterValueList:
    return list(data)
