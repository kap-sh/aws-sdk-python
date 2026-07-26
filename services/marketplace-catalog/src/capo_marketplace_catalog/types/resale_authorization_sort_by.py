"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ResaleAuthorizationSortBy``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: ResaleAuthorizationSortBy) -> str:
    return value


def deserialize_json(data: str) -> ResaleAuthorizationSortBy:
    return cast(ResaleAuthorizationSortBy, data)
