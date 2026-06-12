"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferBuyerAccountsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.offer_buyer_accounts_string

OfferBuyerAccountsList: TypeAlias = list[
    "aws_sdk_marketplace_catalog.types.offer_buyer_accounts_string.OfferBuyerAccountsString"
]


# --- restJson1 ser/de ---
def serialize_json(value: OfferBuyerAccountsList) -> list:
    return list(value)


def deserialize_json(data: list) -> OfferBuyerAccountsList:
    return list(data)
