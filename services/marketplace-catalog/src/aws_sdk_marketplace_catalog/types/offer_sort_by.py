"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferSortBy``."""

from typing import Literal, TypeAlias, cast

OfferSortBy: TypeAlias = Literal[
    "EntityId",
    "Name",
    "ProductId",
    "ResaleAuthorizationId",
    "ReleaseDate",
    "AvailabilityEndDate",
    "BuyerAccounts",
    "State",
    "Targeting",
    "LastModifiedDate",
    "OfferSetId",
]


# --- restJson1 ser/de ---
def serialize_json(value: OfferSortBy) -> str:
    return value


def deserialize_json(data: str) -> OfferSortBy:
    return cast(OfferSortBy, data)
