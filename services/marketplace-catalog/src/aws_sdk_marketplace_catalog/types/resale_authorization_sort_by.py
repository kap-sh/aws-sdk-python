"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ResaleAuthorizationSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_catalog.errors import DeserializationError

ResaleAuthorizationSortBy: TypeAlias = Literal[
    "EntityId",
    "Name",
    "ProductId",
    "ProductName",
    "ManufacturerAccountId",
    "ManufacturerLegalName",
    "ResellerAccountID",
    "ResellerLegalName",
    "Status",
    "OfferExtendedStatus",
    "CreatedDate",
    "AvailabilityEndDate",
    "LastModifiedDate",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EntityId",
        "Name",
        "ProductId",
        "ProductName",
        "ManufacturerAccountId",
        "ManufacturerLegalName",
        "ResellerAccountID",
        "ResellerLegalName",
        "Status",
        "OfferExtendedStatus",
        "CreatedDate",
        "AvailabilityEndDate",
        "LastModifiedDate",
    )
)


def serialize_json(value: ResaleAuthorizationSortBy) -> str:
    return value


def deserialize_json(data: str) -> ResaleAuthorizationSortBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResaleAuthorizationSortBy value: {data!r}")
    return cast(ResaleAuthorizationSortBy, data)
