"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#SaaSProductSortBy``."""

from typing import Literal, TypeAlias, cast

SaaSProductSortBy: TypeAlias = Literal[
    "EntityId",
    "ProductTitle",
    "Visibility",
    "LastModifiedDate",
    "DeliveryOptionTypes",
]


# --- restJson1 ser/de ---
def serialize_json(value: SaaSProductSortBy) -> str:
    return value


def deserialize_json(data: str) -> SaaSProductSortBy:
    return cast(SaaSProductSortBy, data)
