"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#OfferSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_catalog.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: OfferSortBy) -> str:
    return value


def deserialize_json(data: str) -> OfferSortBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OfferSortBy value: {data!r}")
    return cast(OfferSortBy, data)
