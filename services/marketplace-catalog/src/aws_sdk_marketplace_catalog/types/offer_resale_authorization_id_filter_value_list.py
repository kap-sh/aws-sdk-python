"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferResaleAuthorizationIdFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.offer_resale_authorization_id_string

OfferResaleAuthorizationIdFilterValueList: TypeAlias = list[
    "aws_sdk_marketplace_catalog.types.offer_resale_authorization_id_string.OfferResaleAuthorizationIdString"
]


# --- restJson1 ser/de ---
def serialize_json(value: OfferResaleAuthorizationIdFilterValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> OfferResaleAuthorizationIdFilterValueList:
    return list(data)
